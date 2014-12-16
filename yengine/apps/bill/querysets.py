from django.db import models
from django.db.models import Q


class SignatureQuerySet(models.QuerySet):

    def published(self):
        return self.filter(Q(banned=False) & Q(displayed=True))
