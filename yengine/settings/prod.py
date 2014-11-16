from os import environ

from .common import *

import dj_database_url


# Security

SECRET_KEY = environ.get('SECRET_KEY', '')
ALLOWED_HOSTS = (
    'engine.mouvementy.fr',
    'engine.mouvementy.com',
    # 'engine.mouvementy.org',

    'y-engine.herokuapp.com',
)


# Databases

DATABASES = {
    'default': dj_database_url.config(default='')
}


# Apps

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)


# Exception logging

RAVEN_CONFIG = {
    'dsn': environ.get('RAVEN_DNS', ''),
}


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
