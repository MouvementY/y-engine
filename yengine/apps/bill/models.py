from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils import UniqueFilename
from .querysets import SignatureQuerySet


class Signature(models.Model):
    # Tracking fields
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)

    first_name = models.CharField(_("Prénom"),
                                  max_length=150)
    last_name = models.CharField(_("Nom"),
                                 max_length=150)
    email = models.EmailField(_("Email"),
                              unique=True)

    # Accept or not to receive an email on progress
    optin = models.BooleanField(default=True)

    signature_image_data_url = models.TextField(blank=True, null=True)

    # Keep the control if there is an explicit image sent
    # or if the user doesn't want his signature to be public
    banned = models.BooleanField(default=False, db_index=True)
    displayed = models.BooleanField(default=True, db_index=True)

    # Collect the ip address to avoid usage abuses and be able to restore
    # the system in a valid state in case of abuse
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    objects = SignatureQuerySet.as_manager()

    class Meta:
        pass

    def __str__(self):
        return "Signature de {}".format(self.composite_name)

    @property
    def composite_name(self):
        return "{} {}".format(self.first_name, self.last_name)
