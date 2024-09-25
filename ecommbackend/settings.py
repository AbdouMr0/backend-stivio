import os
from pathlib import Path
import django_heroku
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6@mkfzo7=(-sc8r@cl^h(t$m%1^%7fe!1rj^$67jn32k7be6_5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

import dj_database_url
import os

DATABASES = {
    "default": dj_database_url.parse("postgres://stivo_user:xvxSXcHFzinX9jckHHFGhMZcnSxoPKbC@dpg-crnfcdo8fa8c738f976g-a.oregon-postgres.render.com/stivo")
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloth',
    'rest_framework',
    'corsheaders',
    'django_heroku',
]


EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '4acfed7e33a193'
EMAIL_HOST_PASSWORD = '2c8e06f5bedbac'
EMAIL_PORT = '2525'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development server URL
    "https://pn4g26ts-3000.uks1.devtunnels.ms",
    "https://66ede2f3cfd22b7228abd2f5--cheery-alfajores-26ddb5.netlify.app",
    "https://stivio.netlify.app",

]

ROOT_URLCONF = 'ecommbackend.urls'

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

WSGI_APPLICATION = 'ecommbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add these settings to handle media files
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": dj_database_url.parse("postgres://stivo_user:xvxSXcHFzinX9jckHHFGhMZcnSxoPKbC@dpg-crnfcdo8fa8c738f976g-a.oregon-postgres.render.com/stivo")
}
