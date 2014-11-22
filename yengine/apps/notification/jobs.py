from apps.bill.models import Signature
from .clients import (
    PUSH_CHANNEL_SIGNATURE,
    PUSH_EVENTS,

    pusher_client)


# TODO: use the django-rq @job decorator for asynchronicity
def send_new_signature_notification(signature_id):
    """
    Actually send the push notification that has been queued
    to the right shop
    """
    channel = PUSH_CHANNEL_SIGNATURE
    new_count = Signature.objects.all().count()
    pusher_client[channel].trigger('new', {'count': new_count})
