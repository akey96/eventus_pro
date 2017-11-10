#importamos todos las variables q tiene base para q asi podamos trabajar en nuestro entorno de
#desarrollo local
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
# la url de media
MEDIA_URL = '/media/'

# aqui le estamos diciendo q cree una carperta media tomando como base la variable BASE_DIR q es donde esta
# la ruta base del todo_ el proyecto, en esta carpeta media se guardara todos los archivos q vayamos subiendo
# ejemplo :
#       proyecto_Dja.../eventus/media/
MEDIA_ROOT = BASE_DIR.child('media')
