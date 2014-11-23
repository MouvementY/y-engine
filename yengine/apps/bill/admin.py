from django.contrib import admin

from . import models

@admin.register(models.Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date_created',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
