import datetime
from functools import partial
import re

from django.db.models import Count
from django.utils import timezone

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse


def _remove_time(now):
    """Remove the time from the datetime"""
    tz = getattr(now, 'tzinfo', timezone.now().tzinfo)
    return datetime.datetime(now.year, now.month, now.day, tzinfo=tz)


def _to_datetime(dt):
    if isinstance(dt, datetime.datetime):
        return dt
    return _remove_time(dt)


def _parse_interval(interval):
    num = 1
    match = re.match('(\d+)([A-Za-z]+)', interval)

    if match:
        num = int(match.group(1))
        interval = match.group(2)
    return num, interval


def _get_bounds(dt, interval):
    """Returns interval bounds the datetime is in."""

    day = _to_datetime(_remove_time(dt))
    dt = _to_datetime(dt)

    if interval == 'minute':
        begin = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, tzinfo=dt.tzinfo)
        end = begin + relativedelta(minutes=1)
    elif interval == 'hour':
        begin = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, tzinfo=dt.tzinfo)
        end = begin + relativedelta(hours=1)
    elif interval == 'day':
        begin = day
        end = day + relativedelta(days=1)
    elif interval == 'week':
        begin = day - relativedelta(weekday=MO(-1))
        end = begin + datetime.timedelta(days=7)
    elif interval == 'month':
        begin = datetime.datetime(dt.year, dt.month, 1, tzinfo=dt.tzinfo)
        end = begin + relativedelta(months=1)
    elif interval == 'year':
        begin = datetime.datetime(dt.year, 1, 1, tzinfo=dt.tzinfo)
        end = datetime.datetime(dt.year+1, 1, 1, tzinfo=dt.tzinfo)
    else:
        raise InvalidInterval('Inverval not supported.')
    end = end - relativedelta(microseconds=1)
    return begin, end


def _get_interval_sql(date_field, interval):
    """
    Returns SQL clause that calculates the beginning of interval
    date_field belongs to.
    """
    engine_sql = {
        'minutes': "date_trunc('minute', %s)" % date_field,
        'hours': "date_trunc('hour', %s)" % date_field,
        'days': "date_trunc('day', %s)" % date_field,
        'weeks': "date_trunc('week', %s)" % date_field,
        'months': "date_trunc('month', %s)" % date_field,
        'years': "date_trunc('year', %s)" % date_field,
    }

    try:
        return engine_sql[interval]
    except KeyError:
        raise InvalidInterval('Interval is not supported for %s DB backend.' % engine)


class QuerySetStats(object):
    """
    Useful to generate time series.
    """
    def __init__(self, qs=None, date_field=None, aggregate=None, today=None):
        self.qs = qs
        self.date_field = date_field
        self.aggregate = aggregate or Count('id')
        self.today = today or self.update_today()

    # Aggregates for a specific period of time

    def for_interval(self, interval, dt, date_field=None, aggregate=None):
        start, end = _get_bounds(dt, interval)
        date_field = date_field or self.date_field
        kwargs = {'%s__range' % date_field : (start, end)}
        return self._aggregate(date_field, aggregate, kwargs)

    def this_interval(self, interval, date_field=None, aggregate=None):
        method = getattr(self, 'for_%s' % interval)
        return method(self.today, date_field, aggregate)

    # support for this_* and for_* methods
    def __getattr__(self, name):
        if name.startswith('for_'):
            return partial(self.for_interval, name[4:])
        if name.startswith('this_'):
            return partial(self.this_interval, name[5:])
        raise AttributeError

    def time_series(self, start, end=None, interval='days',
                    date_field=None, aggregate=None):
        """Aggregate over time intervals"""
        end = end or self.today
        args = [start, end, interval, date_field, aggregate]
        return self._fast_time_series(*args)

    def _fast_time_series(self, start, end, interval='days',
                          date_field=None, aggregate=None):
        """Aggregate over time intervals using just 1 sql query"""

        date_field = date_field or self.date_field
        aggregate = aggregate or self.aggregate

        num, interval = _parse_interval(interval)

        start, _ = _get_bounds(start, interval.rstrip('s'))
        _, end = _get_bounds(end, interval.rstrip('s'))
        interval_sql = _get_interval_sql(date_field, interval)

        kwargs = {'%s__range' % date_field : (start, end)}
        aggregate_data = self.qs.extra(select = {'d': interval_sql}).\
                        filter(**kwargs).order_by().values('d').\
                        annotate(agg=aggregate)

        today = _remove_time(timezone.now())
        def to_dt(d):
            if isinstance(d, str):
                return parse(d, yearfirst=True, default=today)
            return d

        data = dict((to_dt(item['d']), item['agg']) for item in aggregate_data)

        stat_list = []
        dt = start
        while dt < end:
            idx = 0
            value = 0
            for i in range(num):
                value = value + data.get(dt, 0)
                if i == 0:
                    stat_list.append((dt, value,))
                    idx = len(stat_list) - 1
                elif i == num - 1:
                    stat_list[idx] = (dt, value,)
                dt = dt + relativedelta(**{interval : 1})

        return stat_list

    # Aggregate totals using a date or datetime as a pivot

    def until(self, dt, date_field=None, aggregate=None):
        return self.pivot(dt, 'lte', date_field, aggregate)

    def until_now(self, date_field=None, aggregate=None):
        return self.pivot(compat.now(), 'lte', date_field, aggregate)

    def after(self, dt, date_field=None, aggregate=None):
        return self.pivot(dt, 'gte', date_field, aggregate)

    def after_now(self, date_field=None, aggregate=None):
        return self.pivot(compat.now(), 'gte', date_field, aggregate)

    def pivot(self, dt, operator=None, date_field=None, aggregate=None):
        operator = operator or self.operator
        if operator not in ['lt', 'lte', 'gt', 'gte']:
            raise InvalidOperator("Please provide a valid operator.")

        kwargs = {'%s__%s' % (date_field or self.date_field, operator) : dt}
        return self._aggregate(date_field, aggregate, kwargs)

    def update_today(self):
        self.today = _remove_time(timezone.now())
        return self.today

    def _aggregate(self, date_field=None, aggregate=None, filter=None):
        date_field = date_field or self.date_field
        aggregate = aggregate or self.aggregate

        if not date_field:
            raise DateFieldMissing("Please provide a date_field.")

        if self.qs is None:
            raise QuerySetMissing("Please provide a queryset.")

        agg = self.qs.filter(**filter).aggregate(agg=aggregate)
        return agg['agg']
