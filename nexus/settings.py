"""
Django settings for nexus project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# from django import settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g%0sr+uf-1=bnp_#ya0^j@u@nbteq$=5mf=yya*09f+zvw#nds'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
APPEND_SLASH=True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'categorys',
    'product',
    'user',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
    'blog',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework_simplejwt.authentication.JWTAuthentication',

        )
}
from datetime  import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME":timedelta(minutes=2),
    "REFRESH_TOKEN_LIFETIME":timedelta(days=1),
    "ROTATE_REFRESH_TOKENS":True,
    "BLACKLIST_AFTER_ROTATION":True,
    "UPDATE_LAST_LOGIN":True,
    'TOKEN_OBTAIN_SERIALIZER':'api.serializers.MultiSerializer',
    'ALGORITHM':'HS256',
    # 'SIGNING_KEY':settings.SECRET_KEY,
    'AUDIENCE':'admin'
    # 'JWK_URL':"some-ware.to/path"# aws s3 yoki shunga oxshash serverlardan  malumot ob kelish uchun api reuqest da keladgan sorovlarni yuboryatgan paytda kalitham billa ketish kerak ularga ulanish uchun key lar kerak boladi keylarni esa berilgan manzildan topish mumkin
    
}
SESSION_COOKIE_NAME = "Nurullo"
SESSION_COOKIE_AGE = 3000
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nexus.urls'
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', 

            ],
        },
    },
]


WSGI_APPLICATION = 'nexus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# app/config/settings.py
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',  # TO‘G‘RI BACKEND NOMI
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
         
        'CLIENT_CLASS':'django_redis.client.DefaultClient'

                 }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    BASE_DIR / "static"
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use 465 for SSL
EMAIL_USE_TLS = True 
EMAIL_USE_SSL = False  
EMAIL_HOST_USER = 'qodiraliyevazizbekpdp@gmail.com'
EMAIL_HOST_PASSWORD = 'azizbek1212'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import ssl
ssl._create_default_https_context = ssl._create_unverified_context