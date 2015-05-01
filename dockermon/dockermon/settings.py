"""
Django settings for dockermon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't0@$f5+#k2f9v$5j6f!=m)y31&0t4f^#8-vrda^5cmr%rw8$d)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/main'
SOCIAL_AUTH_TWITTER_KEY ='NWF2Bfb6NVgf35Sd64mItG9DA'
SOCIAL_AUTH_TWITTER_SECRET = 'Nn1ujnXd9rZkM5XzCHJeBysG22JKKaRlaanD253Kb7LJfHSGE2'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '71843179415-gc0ci5oqfuc1snr4uiga8n6gtjl1tole.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='FwNQpapo3fd3Be-WIYgvpvSE'
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True
# Application definition


SOCIAL_AUTH_FACEBOOK_KEY = '1537212706542879'
SOCIAL_AUTH_FACEBOOK_SECRET = '2761bcdd5d563d1bf10b7e3621b8755e'

OAUTH_TOKENS_HISTORY = False # to keep in DB expired access tokens
OAUTH_TOKENS_TWITTER_CLIENT_ID = SOCIAL_AUTH_TWITTER_KEY # application ID
OAUTH_TOKENS_TWITTER_CLIENT_SECRET = SOCIAL_AUTH_TWITTER_SECRET # application secret key
OAUTH_TOKENS_TWITTER_USERNAME = '' # user login
OAUTH_TOKENS_TWITTER_PASSWORD = '' # user password

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dockermon',
    'social.apps.django_app.default',
    'twython',
    'django_instagram'

)
TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)



AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dockermon.urls'

WSGI_APPLICATION = 'dockermon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# Additional locations of static files

STATICFILES_DIRS = [os.path.join(BASE_DIR,     'static')] #very important no path defined yet 
STATIC_URL = '/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')] #very important cos this tells where the templtes are.
