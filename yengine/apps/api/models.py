from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils import UniqueFilename


class Signature(models.Model):
    # Tracking fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    first_name = models.CharField(_("Prénom"),
                                  max_length=150)
    last_name = models.CharField(_("Nom"),
                                 max_length=150)
    email = models.EmailField(_("Email"))

    signature_image = models.ImageField(
        upload_to=UniqueFilename(settings.SIGNATURE_IMAGE_FOLDER))

    class Meta:
        pass

    def __str__(self):
        return "Projet de {}".format(self.client)
