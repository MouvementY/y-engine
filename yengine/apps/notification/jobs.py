import json

from apps.bill.models import Signature
from .clients import (
    PUSH_CHANNEL_SIGNATURE,
    redis_client)


def send_new_signature_notification(signature_instance):
    """
    Actually send the push notification that has been queued
    to the right shop
    """
    channel = PUSH_CHANNEL_SIGNATURE
    new_count = Signature.objects.published().count()

    notification_data = {
            'count': new_count,
            'signature': signature_instance.signature_image_data_url,
            'name': signature_instance.first_name,
        }

    redis_client.publish("notification {}".format(channel),
                         json.dumps(notification_data))
