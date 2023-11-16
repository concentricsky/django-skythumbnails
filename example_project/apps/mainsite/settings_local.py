# settings_local.py is for all instance specific settings


from settings import *
from mainsite import TOP_DIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_ERRORS = True
DEBUG_STATIC = True
DEBUG_MEDIA = True

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'thumbnails',                          # Or path to database file if using sqlite3.
        'USER': 'root',                         # Not used with sqlite3.
        'PASSWORD': '',                     # Not used with sqlite3.
        'HOST': '/tmp/mysql.sock',              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                         # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            "init_command": "SET storage_engine=InnoDB", 
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
        'TIMEOUT': 300,
        'KEY_PREFIX': '',
        'VERSION': 1,
    }
}

# debug_toolbar settings
#MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
#INSTALLED_APPS.append('debug_toolbar')
#INTERNAL_IPS = (
#    '127.0.0.1',
#)
#DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
