
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'misdatos',
        'USER':'alex',
        'PASSWORD':'alekey60254584',
        'HOST':'localhost',
        'PORT':5432
    }
}

STATIC_URL = '/static/'
