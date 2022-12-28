"""
Django dev settings for KETI project.
settings/dev.py
"""
from .base import *

DEBUG = env.DEBUG

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'debug_toolbar',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
