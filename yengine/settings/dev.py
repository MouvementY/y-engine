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
