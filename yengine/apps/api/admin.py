from django.contrib import admin

from . import models


@admin.register(models.Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    pass
