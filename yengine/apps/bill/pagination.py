import six
import collections
import datetime

from django.core.paginator import Paginator, InvalidPage, Page, EmptyPage
from django.db.models import Max, Count, Q, F


class SinceDatePaginator(Paginator):
    """
    A Paginator made for accuracy.

    Large dataset that are updated frequently cannot be explored with
    a standard pagination system, otherwise duplicate would appear if
    a new entry is inserted in the database and a user load the 2nd page.

    That's why we use a **since timestamp** method to paginate results
    """

    def validate_timestamp(self, timestamp):
        """Convert the timestamp into a valid datetime object"""
        if timestamp is None:
            return None

        # Ensure a int value
        try:
            timestamp = int(timestamp)
        except ValueError as exc:
            raise InvalidPage(exc)
        return datetime.datetime.fromtimestamp(timestamp)

    def page(self, date):
        object_list = self.object_list
        if date:
            object_list = object_list.filter(date_created__lte=date)
        object_list = object_list[:self.per_page]
        return DatePage(object_list, date, self)


class DatePage(collections.Sequence):

    def __init__(self, object_list, date, paginator):
        self.object_list = object_list
        self.date = date
        self.paginator = paginator

    def __repr__(self):
        return '<Page %s of %s>' % (self.date, self.paginator.num_pages)

    def __len__(self):
        return len(self.object_list)

    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        # The object_list is converted to a list so that if it was a QuerySet
        # it won't be a database hit per __getitem__.
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]

    def has_next(self):
        # TODO find a way to detect the end
        return True

    def has_previous(self):
        return self.date is not None

    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    def next_page_timestamp(self):
        last_obj = self.object_list[len(self.object_list) - 1]
        last_timestamp = int(last_obj.date_created.timestamp())
        return last_timestamp

    def next_page_number(self):
        raise NotImplementedError("Can't be implemented due the way "
                                  "pagination is working")

    def previous_page_number(self):
        raise NotImplementedError("Can't be implemented due the way "
                                  "pagination is working")

    def start_index(self):
        raise NotImplementedError("Can't be implemented due the way "
                                  "pagination is working")

    def end_index(self):
        raise NotImplementedError("Can't be implemented due the way "
                                  "pagination is working")
