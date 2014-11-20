from django.views import generic
from django.core.urlresolvers import reverse
from django.core.validators import validate_email

from rest_framework import viewsets
from rest_framework import parsers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny

from .models import Signature
from .serializers import SignatureSerializer
from .utils import mailchimp_registrar


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all().order_by('id')
    serializer_class = SignatureSerializer
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser
    )

    # TODO implement a proper authentication flow
    permission_classes = (AllowAny,)

    @list_route(methods=['get'])
    def count(self, request):
        count = self.queryset.count()
        return Response(count)


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
