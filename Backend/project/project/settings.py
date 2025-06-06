"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0^xea*a(p@ye_stqjv_n&=@dolxta@vdj1w7b8sh@g#o$5@y++'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]




INSTALLED_APPS = [
    'unfold',
    # 'jet',  # Add this line before 'django.contrib.admin'
    # 'jazzmin',  # Add this line before 'django.contrib.admin'
    # 'colorfield',  # Required dependency
    # 'admin_interface',  # Custom admin themes
    # 'material',  
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'shop.apps.ShopConfig',
    'rest_framework.authtoken',
    'home.apps.HomeConfig',
    'frontend.apps.FrontendConfig',
    'django_filters',
    'account',
    'corsheaders',
    'community',
    'ai',

]


# Application definition
MATERIAL_ADMIN_SITE = {
    "NAVBAR_BACKGROUND_COLOR": "#000000",  # Black navbar
    "NAVBAR_TEXT_COLOR": "#FFFFFF",  # White text
    "NAVBAR_TAB_BACKGROUND_COLOR": "#1a1a1a",
    "NAVBAR_TAB_TEXT_COLOR": "#FFFFFF",
    "PRIMARY_COLOR": "#000000",  # Black primary color
    "SECONDARY_COLOR": "#333333",  # Dark grey secondary color
}

# Material Admin Theme settings


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    

]
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",  
]
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'project.urls'
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
            ],
        },
    },
]




WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'graduation_project',  
#         'USER': 'postgres', 
#         'PASSWORD': '2002',  
#         'HOST': 'localhost',  
#         'PORT': '5432',  
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'grovana',
        'USER': 'grovana',
        'PASSWORD': 'grovana1234',
        'HOST': 'grovana.cha8yi6yse97.eu-north-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Password hashing settings AUTHENTICATION
REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
   
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# Password validation settings AUTHENTICATION
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'BLACKLIST_AFTER_ROTATION': True,
    "AUTH_HEADER_TYPES": ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
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

CORS_ALLOW_ALL_ORIGINS = True 

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

# Keep your development static files (like your own CSS, JS, images)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Store collected static files separately (used for production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'grovanastore@gmail.com'
EMAIL_HOST_PASSWORD = 'kqiq vcok fewb wvjv'
AUTH_USER_MODEL = 'account.User'
