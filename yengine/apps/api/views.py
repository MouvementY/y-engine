from django.views import generic
from django.core.urlresolvers import reverse

from rest_framework import viewsets
from rest_framework import parsers
from rest_framework.permissions import AllowAny

from .models import Signature
from .serializers import SignatureSerializer


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
    parser_classes = (
        parsers.MultiPartParser,
        parsers.FormParser,
        parsers.JSONParser
    )

    # TODO implement a proper authentication flow
    permission_classes = (AllowAny,)
