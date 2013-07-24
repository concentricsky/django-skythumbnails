import sys
import os

from mainsite import TOP_DIR


##
#
#  Important Stuff
#
##

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'mainsite',

    # Include sky-Thumbnails in your project apps list
    'sky_thumbnails',

    'south',

    'photos',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mainsite.urls'

SECRET_KEY = '{{secret_key}}'


##
#
#  Templates
#
##

TEMPLATE_LOADERS = [
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_DIRS = [
    os.path.join(TOP_DIR, 'breakdown', 'templates'),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
]

JINGO_EXCLUDE_APPS = ('admin', 'registration', 'debug_toolbar')


##
#
#  Static Files
#
##

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(TOP_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(TOP_DIR, 'breakdown', 'static'),
]


##
#
#  Media Files
#
##

MEDIA_ROOT = os.path.join(TOP_DIR, 'mediafiles')
MEDIA_URL = '/media/'


##
#
# Thumbnails Settings
#
##

THUMBNAILS_DELAYED_GENERATION = True
THUMBNAILS_DIRNAME = 'thumbnails'

##
#
#   Fixtures
#
##

FIXTURE_DIRS = [
    os.path.join(TOP_DIR, 'etc', 'fixtures'),
]


##
#
#  Logging
#
##

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


##
#
#  Misc.
#
##

SITE_ID = 1

USE_I18N = False
USE_L10N = False
USE_TZ = True

##
#
#  Import settings_local.
#
##

try:
    from settings_local import *
except ImportError as e:
    import sys
    sys.stderr.write("no settings_local found, setting DEBUG=True...\n")
    DEBUG = True
    pass
