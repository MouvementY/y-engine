from django.db import models


class Blacklist(models.Model):
    ip_address = models.GenericIPAddressField("IP address",
                                              max_length=18)

    readonly = models.BooleanField("Readonly authorize",
                                   default=True)

    class Meta:
        pass

    def __str__(self):
        return "IP: {} ({})".format(self.ip_address, self.mode)

    @property
    def mode(self):
        if self.readonly:
            return "readonly"
        return "strict"
