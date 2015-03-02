from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .querysets import PostQuerySet


class Post(models.Model):
    # Tracking fields
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)

    date_published = models.DateTimeField(default=timezone.now,
                                          db_index=True)
    title = models.CharField(_("Titre"),
                             max_length=150)
    text = models.TextField(_("Texte"),
                            blank=True, null=True)
    link = models.URLField(_("Lien"),
                           blank=True, null=True)

    objects = PostQuerySet.as_manager()

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.title)
