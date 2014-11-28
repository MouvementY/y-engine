import datetime

from django.views import generic
from django.core.urlresolvers import reverse
from django.core.validators import validate_email

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

from apps.bill.models import Signature
from .serializers import SignatureSerializer, SignatureCreationSerializer
from .utils import mailchimp_registrar
from .stats import QuerySetStats


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.published().order_by('-id')
    serializer_class = SignatureSerializer
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser
    )

    # TODO implement a proper authentication flow
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'create':
            return SignatureCreationSerializer
        return super().get_serializer_class()

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
        today = datetime.date.today()
        seven_days_ago = today - datetime.timedelta(days=7)
        week_stats = stats_queryset.time_series(seven_days_ago,
                                                today,
                                                interval='hours')

        return Response(week_stats)


class SubscribeToEventNotificationsView(APIView):
    permission_classes = (AllowAny,)

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
