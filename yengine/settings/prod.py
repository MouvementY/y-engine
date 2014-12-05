from os import environ
from urllib.parse import urlparse

from .common import *

import dj_database_url


# Security

SECRET_KEY = environ.get('SECRET_KEY', '')
ALLOWED_HOSTS = (
    'engine.mouvementy.fr',
    'engine.mouvementy.com',
    # 'engine.mouvementy.org',

    'y-engine.herokuapp.com',
    'y-engine-staging.herokuapp.com',
)


# Databases

DATABASES = {
    'default': dj_database_url.config(default='')
}


# Redis

REDIS = urlparse(environ.get('REDISCLOUD_URL', ''))


# Apps

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)


# Exception logging

RAVEN_CONFIG = {
    'dsn': environ.get('RAVEN_DNS', ''),
}


# Mandrill/Mailchimp

MAILCHIMP_API_KEY = environ.get('MAILCHIMP_API_KEY', '')

MAILCHIMP_EVENTS_NOTIFICATION_LIST_ID = environ.get('MAILCHIMP_EVENTS_NOTIFICATION_LIST_ID', '')


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'no_formatting': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'sentry'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console', 'sentry'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'sentry'],
            'propagate': False,
            'level':'ERROR',
        },

        'apps': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}


# Pusher

PUSHER = urlparse(environ.get('PUSHER_URL', ''))
PUSHER_KEY = PUSHER.username
PUSHER_SECRET = PUSHER.password
PUSHER_HOST = PUSHER.hostname
PUSHER_APP_ID = PUSHER.path.split('/')[-1]  # last path component


# Loader.io

LOADERIO_ENABLED = bool(int(environ.get('LOADERIO_ENABLED', '0')))
LOADERIO_TOKEN = environ.get('LOADERIO_TOKEN', '')
