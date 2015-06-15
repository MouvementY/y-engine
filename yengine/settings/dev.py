import os
from urllib.parse import urlparse

from .common import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = '56!^41_3z2tgd@a^d^95r&80*pn_@(+&@&l=163g@ho_)a&1ui'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yengine',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar.apps.DebugToolbarConfig',
    )


# Redis

REDIS = urlparse('redis://localhost:6379')


# Mandrill/Mailchimp

MAILCHIMP_API_KEY = '5d3e2bd361da8960889ae28f670f037f-us6'

MAILCHIMP_EVENTS_NOTIFICATION_LIST_ID = '21b36a9897'


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
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': False,
            'level':'ERROR',
        },

        'apps': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


# Pusher

PUSHER = urlparse("http://6f721c613fa6823eb3a5:5464dcf3a8ba9b5400c3@api-eu.pusher.com/apps/97556")
PUSHER_KEY = PUSHER.username
PUSHER_SECRET = PUSHER.password
PUSHER_HOST = PUSHER.hostname
PUSHER_APP_ID = PUSHER.path.split('/')[-1]  # last path component


# Loader.io

LOADERIO_ENABLED = False
LOADERIO_TOKEN = ""
