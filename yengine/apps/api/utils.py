import logging

from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

from mailsnake import MailSnake

logger = logging.getLogger(__name__)


class MailchimpRegistrar(object):
    _mail_snake = None

    def __init__(self):
        if not hasattr(settings, 'MAILCHIMP_API_KEY'):
            logger.error('MailChimp API key not present')
        self._mail_snake = MailSnake(settings.MAILCHIMP_API_KEY)

    def _register_email(self, email, list_id):
        self._mail_snake.listSubscribe(id=list_id,
                                       email_address=email,
                                       merge_vars={'EMAIL': email},
                                       double_optin=True,
                                       update_existing=True)

    def subscribe_to_events_notification(self, email):
        list_id = settings.MAILCHIMP_EVENTS_NOTIFICATION_LIST_ID
        self._register_email(email, list_id)


# singleton
mailchimp_registrar = MailchimpRegistrar()
