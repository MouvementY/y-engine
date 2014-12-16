from django.contrib import admin

from . import models


@admin.register(models.Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date_created',
        '_is_published',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    fields = (
        'banned',
        'displayed',
        'ip_address',
        'first_name',
        'last_name',
        'email',
        'optin',

        'signature_image_data_url',
        '_get_signature_image',
    )
    readonly_fields = (
        '_get_signature_image',
    )

    def _is_published(self, obj):
        return (obj.displayed and not obj.banned)
    _is_published.boolean = True

    def _get_signature_image(self, obj):
        return "<img src=\"{}\"/>".format(obj.signature_image_data_url)
    _get_signature_image.allow_tags = True
    _get_signature_image.short_description = "Signature"
