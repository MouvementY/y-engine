import logging

from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

from mailsnake import MailSnake

logger = logging.getLogger(__name__)


def add_email_to_mailchimp(email):

    # Check first if the mailchimp key is present.
    if not hasattr(settings, 'LANDING_MAILCHIMP_API'):
        logger.error('MailChimp API not present')
        return
    mailchimp_api = settings.LANDING_MAILCHIMP_API

    # Check for mailchimp list.
    if not hasattr(settings, 'LANDING_MAILCHIMP_LIST'):
        logger.error('MailChimp List not defined')
        return
    mailchimp_list = settings.LANDING_MAILCHIMP_LIST

    # Subscribe user to list.
    ms = MailSnake(mailchimp_api)
    ms.listSubscribe(
        id=mailchimp_list,
        email_address=email,
        merge_vars={'EMAIL': email},
        double_optin=True,
        update_existing=True)
