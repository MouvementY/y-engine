from rest_framework import serializers

from apps.news.models import Post
from apps.bill.models import Signature
from apps.bill.filters import ImageConvertor, DotSignatureIdentifierProcessor


class SignatureCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signature
        fields = (
            'first_name',
            'last_name',
            'email',
            'optin',
            'signature_image_data_url',
        )

    def validate_signature_image_data_url(self, value):
        """
        Avoid getting dot-based signatures or blank ones
        """
        if value is None:
            # already sanitized
            return None

        # a typical threshold of 1% let us detect the dot-based signatures
        convertor = ImageConvertor()
        processor = DotSignatureIdentifierProcessor(threshold=0.01)

        try:
            img = convertor.image_from_data_uri(value)
        except ValueError:
            return None

        ratio = processor.get_colored_pixel_ratio(img)
        if ratio < processor.threshold:
            return None

        return value


class SignatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signature
        fields = ('first_name', 'signature_image_data_url',)
        read_only_fields = ('first_name', 'signature_image_data_url',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', 'link', 'date_published',)
