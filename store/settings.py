# Django settings for satchmo project.
# This is a recommended base setting for further customization

import django
import os

DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
DIRNAME = os.path.dirname(__file__)

DJANGO_PROJECT = 'store'
DJANGO_SETTINGS_MODULE = 'store.settings'

ADMINS = (
     ('laura', 'laura@emlprime.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
# The following variables should be configured in your local_settings.py file
DATABASE_NAME = 'db_data'             # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# Image files will be stored off of this path
#
# If you are using Windows, recommend using normalize_path() here
#
# from satchmo_utils.thumbnail import normalize_path
# MEDIA_ROOT = normalize_path(os.path.join(DIRNAME, 'static/'))
MEDIA_ROOT = os.path.join(DIRNAME, 'static/')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL="/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$wbh_702sn#@r707&aerqkcc4g6%4bn%)k5s3@yhya5&#uhii#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#      'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    "satchmo_ext.recentlist.middleware.RecentProductMiddleware",
    #'djangologging.middleware.LoggingMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#this is used to add additional config variables to each request
# NOTE: If you enable the recent_products context_processor, you MUST have the
# 'satchmo_ext.recentlist' app installed.
TEMPLATE_CONTEXT_PROCESSORS = (
    'satchmo_store.shop.context_processors.settings',
    'django.core.context_processors.auth',
#     'satchmo_ext.recentlist.context_processors.recent_products',
    )

ROOT_URLCONF = 'store.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    SITE_ROOT + '/templates/'
)

INSTALLED_APPS = (
    'django.contrib.sites',
    'satchmo_store.shop',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'registration',
    'sorl.thumbnail',
    'keyedcache',
    'livesettings',
    'l10n',
    'satchmo_utils.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    #'satchmo_store.contact.supplier',
    #'shipping.modules.tiered',
    #'satchmo_ext.newsletter',
    'satchmo_ext.recentlist',
    #'testimonials',
    'product',
    #'satchmo_ext.product_feeds',
    #'satchmo_ext.brand',
    'payment',
    'payment.modules.dummy',
    #'payment.modules.purchaseorder',
    #'payment.modules.giftcertificate',
    #'satchmo_ext.wishlist',
    #'satchmo_ext.upsell',
    #'satchmo_ext.productratings',
    'satchmo_ext.satchmo_toolbar',
    'satchmo_utils',
    #'shipping.modules.tieredquantity',
    #'satchmo_ext.tieredpricing',
    #'typogrify',
    #'debug_toolbar',
    'app_plugins',
    'store.localsite',
)

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS' : False,
#}

#### Satchmo unique variables ####
#from django.conf.urls.defaults import patterns, include
SATCHMO_SETTINGS = {
    'SHOP_BASE' : '',
    'MULTISHOP' : False,
    #'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

# Load the local settings
from local_settings import *
