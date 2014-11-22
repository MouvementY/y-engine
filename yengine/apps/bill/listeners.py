from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.bill.models import Signature
from apps.notification.jobs import (
    send_new_signature_notification)


@receiver(post_save, sender=Signature)
def handle_order_is_saved(sender, instance, created, **kwargs):
    if getattr(instance, '_disable_pusher_notification', False):
        return

    # queue = django_rq.get_queue('default')
    # queue.enqueue(send_new_signature_notification, instance.id)
    # TODO use rq
    send_new_signature_notification(instance.id)
