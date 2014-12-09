import datetime

from django.views import generic
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.paginator import InvalidPage
from django.http import Http404

from rest_framework import viewsets
from rest_framework import parsers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import (
    detail_route,
    list_route,
    permission_classes)
from rest_framework.permissions import AllowAny, IsAdminUser
from ipware.ip import get_real_ip

from apps.bill.models import Signature
from apps.bill.pagination import SinceDatePaginator
from .permissions import BlacklistPermission
from .serializers import SignatureSerializer, SignatureCreationSerializer
from .pagination import DatePaginationSerializer
from .utils import mailchimp_registrar
from .stats import QuerySetStats


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.published().order_by('-date_created')
    serializer_class = SignatureSerializer
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser
    )
    pagination_serializer_class = DatePaginationSerializer
    paginator_class = SinceDatePaginator
    paginate_by = 64
    page_kwarg = 'before'

    permission_classes = (BlacklistPermission, AllowAny,)
    throttle_scope = 'signatures'

    def get_serializer_class(self):
        if self.action == 'create':
            return SignatureCreationSerializer
        return super().get_serializer_class()

    def paginate_queryset(self, queryset, page_size=None):
        """
        Paginate a queryset if required, either returning a page object,
        or `None` if pagination is not configured for this view.
        """
        page_size = self.get_paginate_by()
        if not page_size:
            return None

        paginator = self.paginator_class(queryset, page_size)
        page_kwarg = self.kwargs.get(self.page_kwarg)
        page_query_param = self.request.query_params.get(self.page_kwarg)
        page = page_kwarg or page_query_param or None
        try:
            ref_timestamp = paginator.validate_timestamp(page)
        except InvalidPage:
            if page is None:
                ref_timestamp = None
            else:
                raise Http404("Page is not 'last', nor can it be converted to an int.")

        try:
            page = paginator.page(ref_timestamp)
        except InvalidPage as exc:
            error_format = 'Invalid page (%(ref_timestamp)s): %(message)s'
            raise Http404(error_format % {
                'ref_timestamp': ref_timestamp,
                'message': six.text_type(exc)
            })

        return page

    def perform_create(self, serializer):
        ip = get_real_ip(self.request)
        serializer.save(ip_address=ip)

    @list_route(methods=['get'])
    def count(self, request):
        count = self.queryset.count()
        return Response(count)

    @list_route(methods=['get'])
    # @permission_classes([IsAdminUser])
    def timeseries(self, request):
        queryset = self.get_queryset()
        stats_queryset = QuerySetStats(queryset, 'date_created')

        # compute time series on the last week
        launch = datetime.date(2014, 11, 20)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        interval = request.GET.get('interval', 'hours')
        week_stats = stats_queryset.time_series(launch,
                                                tomorrow,
                                                interval=interval)

        return Response(week_stats)


class SubscribeToEventNotificationsView(APIView):
    permission_classes = (AllowAny,)
    throttle_scope = 'subscriptions'

    def post(self, request, *args, **kwargs):
        email = request.DATA.get('email', None)
        if not email:
            return Response({"detail": "Le champ semble si vide..."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except:
            return Response({"detail": "L'adresse email semble invalide"},
                            status=status.HTTP_400_BAD_REQUEST)

        mailchimp_registrar.subscribe_to_events_notification(email)
        return Response({"detail": "Merci. Vous venez de recevoir un mail "
                                   "de confirmation"},
                        status=status.HTTP_201_CREATED)
