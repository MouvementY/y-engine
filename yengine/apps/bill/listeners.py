import logging

from django.dispatch import receiver
from django.db.models.signals import post_save

from redis.exceptions import ConnectionError

from apps.bill.models import Signature
from apps.notification.jobs import (
    send_new_signature_notification)

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Signature)
def handle_signature_is_saved(sender, instance, created, **kwargs):
    # not a new signature
    if not created:
        # TODO, send the remove signature signal if it has been banned
        return

    if getattr(instance, '_disable_pusher_notification', False):
        return

    try:
        send_new_signature_notification(instance)
    except ConnectionError as exc:
        logger.error(exc)
