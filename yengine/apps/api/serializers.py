from rest_framework import serializers

from .models import Signature


class SignatureCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signature


class SignatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signature
        fields = ('first_name', 'signature_image_data_url',)
        read_only_fields = ('first_name', 'signature_image_data_url',)
