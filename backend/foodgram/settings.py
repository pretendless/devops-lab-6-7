import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.environ.get('DEBUG', True)

if DEBUG:
    SECRET_KEY = 'debug'
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '*']

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']

CORS_URLS_REGEX = r'^/api/.*$'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'import_export',
    'rest_framework.authtoken',
    'djoser',

    'users',
    'api',
    'recipes'
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

ROOT_URLCONF = 'foodgram.urls'

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

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
        }
    }

WSGI_APPLICATION = 'foodgram.wsgi.application'

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'PAGE_SIZE': 6,
}

DJOSER = {
    'LOGIN_FIELD': 'email',

    'HIDE_USERS': False,
    'SERIALIZERS': {
        'user': 'users.serializers.UserSerializer',
        'current_user': 'users.serializers.UserSerializer'
    },

    'PERMISSIONS': {
        'activation': ['rest_framework.permissions.AllowAny'],
        'password_reset': ['rest_framework.permissions.AllowAny'],
        'password_reset_confirm': ['rest_framework.permissions.AllowAny'],
        'set_password': ['djoser.permissions.CurrentUserOrAdmin'],
        'username_reset': ['rest_framework.permissions.AllowAny'],
        'username_reset_confirm': ['rest_framework.permissions.AllowAny'],
        'set_username': ['djoser.permissions.CurrentUserOrAdmin'],
        'user_create': ['rest_framework.permissions.AllowAny'],
        'user_delete': ['djoser.permissions.CurrentUserOrAdmin'],
        'user': ['rest_framework.permissions.AllowAny'],
        'user_list': ['rest_framework.permissions.AllowAny'],
        'token_create': ['rest_framework.permissions.AllowAny'],
        'token_destroy': ['rest_framework.permissions.IsAuthenticated'],
    }
}

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/backend_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'backend_static')

MEDIA_URL = '/backend_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'backend_media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
