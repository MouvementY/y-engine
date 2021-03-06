from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date_created',
    )
