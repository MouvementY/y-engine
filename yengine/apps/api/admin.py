# encoding: utf-8

from django.contrib import admin

from apps.api import models


admin.site.register(models.Signature)
