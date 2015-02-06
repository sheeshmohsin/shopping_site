"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from configurations import Configuration, values

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

class Common(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'l4rk9bh$pz8g#!7z_)10x(_v8+e4-iz37i2!ugc2v)@(@5k28*'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []
    # APP CONFIGURATION
    # -----------------
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'bootstrap3',
    )

    LOCAL_APPS = (
        # Your stuff: custom apps go here
        'users',  # custom users app
        'core',
        'explore',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    INSTALLED_APPS += (
        # Needs to come last for now because of a weird edge case between
        #   South and allauth
        'allauth',  # registration
        'allauth.account',  # registration
        'allauth.socialaccount',  # registration
        'allauth.socialaccount.providers.google',
        'allauth.socialaccount.providers.github',
    )

    SITE_ID = 1

    SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}

    LOGIN_REDIRECT_URL = '/'

    SOCIALACCOUNT_QUERY_EMAIL = True

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.request",
        "allauth.account.context_processors.account",
        "django.contrib.auth.context_processors.auth",
        "allauth.socialaccount.context_processors.socialaccount",
        "explore.context_processors.category_list",
    )

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    ROOT_URLCONF = 'app.urls'

    WSGI_APPLICATION = 'app.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates')
    )
    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    STATIC_ROOT = join(BASE_DIR, 'staticfiles')

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')
 
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION
 

class Dev(Common):
    DEBUG = True
