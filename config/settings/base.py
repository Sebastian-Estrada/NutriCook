import environ
import json
import os

from dotenv import load_dotenv

load_dotenv()


ROOT_DIR = environ.Path(__file__) - 3
BASE_DIR = ROOT_DIR
APPS_DIR = ROOT_DIR.path('apps')

ALLOWED_HOSTS = os.getenv('OWN_DOMAINS', '').split(',')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
AUTH_USER_MODEL = 'users.User'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = 'users:login'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = 'users:login'

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')

SESSION_SAVE_EVERY_REQUEST = True
SITE_ID = 1
TIME_ZONE = 'Canada/Eastern'
USE_I18N = True
USE_L10N = False
USE_TZ = False

DATE_INPUT_FORMATS = ["%Y-%m-%d", ]
DATETIME_FORMAT = "Y-m-d h:i a"

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASE_DEFAULT = json.loads(os.getenv('DATABASE_DEFAULT'))
DATABASES = {

}
DATABASES = {
    'default':DATABASE_DEFAULT
}

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',
    'django_extensions',

]
THIRD_PARTY_APPS = [
    'bootstrap4',
    'django_select2',
]

PUBLIC_APPS = [
    'apps.core',
    'apps.cuisine_types',
    'apps.dashboards',
    'apps.ingredients',
    'apps.meal_types',
    'apps.meal_planner',
    'apps.meals',
    'apps.recipes',
    'apps.users',
]


SHARED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PUBLIC_APPS

INSTALLED_APPS = SHARED_APPS

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('../staticfiles'))

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
    str(APPS_DIR.path('media')),
]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = str(APPS_DIR('media'))

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of allauth
    'django.contrib.auth.backends.ModelBackend',
]

INITIAL_USER = json.loads(os.getenv('INITIAL_USER'))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

# Redis database index for Select2 data
SELECT2_DB = 2

# URL for Redis cache store for Select2
SELECT2_CACHE_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{SELECT2_DB}'

CACHES = {
    'select2': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': SELECT2_CACHE_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': SELECT2_CACHE_URL,
    },
}

SELECT2_CACHE_BACKEND = 'select2'
