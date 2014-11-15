from os import environ

from .common import *

import dj_database_url


DATABASES = {
    'default': dj_database_url.config(default='')
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': environ.get('RAVEN_DNS', ''),
}
