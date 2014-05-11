import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


DEBUG = get_env_variable("DJANGO_DEBUG")
if DEBUG == 1 or DEBUG == '1' or DEBUG == 'True':
    DEBUG = True
else:
    DEBUG = False

LOCAL_DEV = get_env_variable("DJANGO_LOCAL_DEV")
if LOCAL_DEV == 1 or LOCAL_DEV == '1' or LOCAL_DEV == 'True':
    LOCAL_DEV = True
else:
    LOCAL_DEV = False

DATABASES = {}

if LOCAL_DEV:
    ALLOWED_HOSTS = ['*']  # useful when testing with DEBUG = FALSE
    INTERNAL_IPS = ('127.0.0.1',)  # sets local IPS needed for DEBUG_TOOLBAR and other items.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'materialsapp',
            'USER': 'ashlee',
            'PASSWORD': 'ashleepw',
            'HOST': 'localhost',
            'PORT': ''
        }
    }

else:
    # Parse database configuration from $DATABASE_URL
    ALLOWED_HOSTS = ['materialsapp.herokuapp.com']

    import dj_database_url
    dbconfig = dj_database_url.config()
    if dbconfig:
        DATABASES['default'] = dbconfig

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = get_env_variable('SECRET_KEY')

THUMBNAIL_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'dajaxice',
    'dajax',
    'debug_toolbar',
    'sorl.thumbnail',
    'storages',
    'south'
)

MY_APPS = (
    'core',
    'cuts',
    'finishes',
    'forms',
    'joins',
    'materials'
)

INSTALLED_APPS += MY_APPS

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request',)
TEMPLATE_LOADERS = DEFAULT_SETTINGS.TEMPLATE_LOADERS + ('django.template.loaders.eggs.Loader',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'materialsapp.urls'

WSGI_APPLICATION = 'materialsapp.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/media/'
STATIC_ROOT = BASE_DIR + '/collected_static/'

STATICFILES_FINDERS = DEFAULT_SETTINGS.STATICFILES_FINDERS + ('dajaxice.finders.DajaxiceFinder',)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

import sqlparse
import logging


class sqlformatter(logging.Formatter):
    def format(self, record):
        if record.sql:
            return '\n' + sqlparse.format(record.sql, reindent=True, keyword_case='upper') + '\n'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'sqlformatter': {
            '()': sqlformatter
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'console_sql': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sqlformatter'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True
        }
    }
}


AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'core.storage.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    STATICFILES_STORAGE = 'core.storage.StaticStorage'
    STATIC_S3_PATH = 'static'
    AWS_STORAGE_BUCKET_NAME = 'media.materialsapp'
    AWS_STATIC_BUCKET_NAME = 'static.materialsapp'
    MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STATIC_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    AWS_S3_SECURE_URLS = False

# breaks urlpatterns if True
DEBUG_TOOLBAR_PATCH_SETTINGS = False
