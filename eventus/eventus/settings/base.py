"""en este archivo ira todos las configuraciones basicas para el funcionamiento en forma global
del proyecto"""
#encoding:utf-8
import os
# importamos este paquete q instalamos a nuestro entorno, q nos permite interacutar con las
#rutas de los archovos q vendira a reemplazar a la libreria  os
from unipath import Path

# modificamos esta varible que tome como RutaBase, 3 nieveles atras de donde esta este archivo
#, es decir donde estan todas las direcoritos como ser(apps,eventus,manage.py,..etc)
BASE_DIR = Path(__file__).ancestor(3)
SECRET_KEY = '$eokgygj!zb%zak3r__t0dfzxd0$x55zu^k=muwypk@__7tnj5'
DEBUG = True

ALLOWED_HOSTS = []

#esta variable almacena las apps que trae Django por defecto
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#esta variable  almacena las apps que nosotros desarrollaremos e implemetaremos para nuestro proyecto
LOCAL_APPS = [
    'apps.events',
    'apps.users',
]

#esta variable almacena las apps que implementaremos pero de 3ras personas
THIRD_PARTY_APP = []

#como sabran Django, busta globalmente en esta variable todas las apps con que cuenta nuestro
#proyecto, es por eso que lo almacenamos todo en esta variable
INSTALLED_APPS = DJANGO_APPS+LOCAL_APPS+THIRD_PARTY_APP

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eventus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eventus.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'es-BO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#esta variable contiene la ruta en donde esta las clases de nuestro User personalisado
#que vamos a utilizar para hacer referencia al User personalizado
AUTH_USER_MODEL = 'users.User'