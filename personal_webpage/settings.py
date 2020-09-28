from os import path, environ
from pathlib import Path
from dotenv import load_dotenv

SECRET_KEY = 'SECRET_KEY'
DEBUG_KEY = 'DEBUG'
ALLOWED_HOSTS = 'ALLOWED_HOSTS'
ENV = 'ENV'

DB_NAME = 'BD_NAME'
DB_HOST = 'DB_HOST'
DB_USER = 'DB_USER'
DB_PASSWORD = 'DB_PASSWORD'

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
load_dotenv(path.join(BASE_DIR, '.env'))

SECRET_KEY = environ[SECRET_KEY]

DEBUG = bool(environ.get(DEBUG_KEY, 0))

ALLOWED_HOSTS = [environ[ALLOWED_HOSTS]]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',
    'projects'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personal_webpage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'personal_webpage.wsgi.application'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

if environ[ENV] == 'prod':
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'personal-webpage-static'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ[DB_NAME],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'USER': environ[DB_USER],
        'PASSWORD': environ[DB_PASSWORD],
        'HOST': environ[DB_HOST],
        'PORT': '3306'
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
    BASE_DIR / 'personal_webpage' / 'static'
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
