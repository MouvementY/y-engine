from django.db import models


class Blacklist(models.Model):
    ip_address = models.GenericIPAddressField("IP address",
                                              max_length=18)

    readonly = models.BooleanField("Readonly authorize",
                                   default=True)

    def __self__(self):
        return "IP: %s" % self.ip_address

    class Meta:
        pass
