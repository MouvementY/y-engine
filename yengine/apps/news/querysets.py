from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):

    def published(self):
        now = timezone.now()
        return self.filter(date_published__lte=now)
