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

    # TODO fill the image field with the base64 encoded value
    signature_image = models.ImageField(
        upload_to=UniqueFilename(settings.SIGNATURE_IMAGE_FOLDER),
        blank=True, null=True)
    signature_image_data_url = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return "Signature de {}".format(self.composite_name)

    @property
    def composite_name(self):
        return "{} {}".format(self.first_name, self.last_name)
