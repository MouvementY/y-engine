from rest_framework import serializers
from rest_framework import pagination
from rest_framework.templatetags.rest_framework import replace_query_param


class NextTimestampPageField(serializers.Field):
    """
    Field that returns a link to the next page in paginated results.
    """
    page_field = 'before'

    def to_representation(self, value):
        if not value.has_next():
            return None
        timestamp = value.next_page_timestamp()
        request = self.context.get('request')
        url = request and request.build_absolute_uri() or ''
        return replace_query_param(url, self.page_field, timestamp)


class DatePaginationSerializer(pagination.BasePaginationSerializer):
    next = NextTimestampPageField(source='*')
    count = serializers.ReadOnlyField(source='paginator.count')

    results_field = 'results'
