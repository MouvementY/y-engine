from django.db import models


class SignatureQuerySet(models.QuerySet):

    def published(self):
        return self.filter(banned=False)
