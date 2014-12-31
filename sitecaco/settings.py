"""
Django settings for sitecaco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#Aqui são mantidas as variáveis específicas a plataforma
from sitecaco.local_settings import *


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SITE_ID = 1


ALLOWED_HOSTS = []

MEDIA_URL = '/media/'
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')


# Application definition

INSTALLED_APPS = (
    'django_forms_bootstrap',
    'sitecaco',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.auth',
    'haystack',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sitecaco.urls'

WSGI_APPLICATION = 'sitecaco.wsgi.application'




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
   "django.contrib.auth.context_processors.auth",
   "django.core.context_processors.request",
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(ENV_PATH, 'static/');
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)




