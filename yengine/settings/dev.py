import os

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
        'OPTIONS': {
            'autocommit': True,
        },
    }
}


if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar.apps.DebugToolbarConfig',
    )


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
