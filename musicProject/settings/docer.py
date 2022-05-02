DEBUG = True

from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'musicDatabase',
        'HOST': 'db',
        'USER': 'USER_NAME',
        'PASSWORD': 'supersecret',
        'PORT': '5432',
    }
}