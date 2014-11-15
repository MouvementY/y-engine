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
