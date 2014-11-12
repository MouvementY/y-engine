from django.views import generic
from django.core.urlresolvers import reverse

from rest_framework import viewsets

from .models import Signature
from .serializers import SignatureSerializer


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
