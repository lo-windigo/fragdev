# This file is part of the FragDev Website.
# 
# the FragDev Website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# the FragDev Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the FragDev Website.  If not, see <http://www.gnu.org/licenses/>.

from os import path
import os
import stat
import yaml


##################
# Local settings #
##################

PROJECT_APP_PATH = path.dirname(os.path.abspath(__file__))
local_config_path = path.join(PROJECT_APP_PATH, "local.yaml")

if not path.exists(local_config_path):
    raise Exception("Missing local.yaml")

local_settings_file = open(local_config_path, 'r')
local_settings = yaml.full_load(local_settings_file)
required_configs = (
        'domain', 'secret_key', 'database', 'media_path',
        'static_path', 'webroot'
        )

# Check for all the required configuration values
for required_config in required_configs:
    if not required_config in local_settings:
        msg = 'Missing required configuration: {}'.format(required_config)
        raise Exception(msg)

# Pull out all of the local configurations
DEBUG = local_settings.get('debug', False) == 'True'
DOMAIN = local_settings.get('domain')
SECRET_KEY = local_settings.get('secret_key')
WEBROOT = local_settings.get('webroot')

# Parse the DB configurations
db_settings = local_settings.get('database')
db_type = db_settings.get('type', 'Unspecified')

# Build the database configurations for supported types
if db_type == 'sqlite':
    db_path = db_settings.get('path')
    database = {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": path.join(WEBROOT, db_path),
        }
elif db_type == 'mysql':
    # TODO: we would need to add local config parsing to use this
    database = {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "database_name",
        "USER": "database_user",
        "PASSWORD": "password",
        "HOST": "", # Set to empty string for localhost.
        "PORT": "", # Set to empty string for default.
    }
else:
    raise Exception('Unsupported DB type: {}'.format(db_type))


##########################
# Contact script details #
##########################

CONTACT_EMAIL = 'admin@{}'.format(DOMAIN)
CONTACT_SENDER= 'website@{}'.format(DOMAIN)
CONTACT_SUBJECT = 'Message from {}'.format(DOMAIN)


########################
# Time / Date settings #
########################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = local_settings.get('timezone', 'UTC')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


#######################
# File configurations #
#######################

# Default filesystem permissions for uploaded files
FILE_UPLOAD_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP

# File paths for static/media files
MEDIA_ROOT = path.join(WEBROOT, 'srv/media')
STATIC_ROOT = path.join(WEBROOT, 'srv/static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# URL prefix for static files.
STATIC_URL = '/static/'


#########################
# Django configurations #
#########################

# Site administrators
ADMINS = (
     ('Administrator', 'admin@{}'.format(DOMAIN)),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
ALLOWED_HOSTS = [
        '127.0.0.1',
        DOMAIN,
        '.{}'.format(DOMAIN)
        ]

# Specify what field type is used for automatic primary keys
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Use database configuration passed in from the local settings
DATABASES = { "default": database }

# List of callables that know how to import templates from various sources.
MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fragdev.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'fragdev.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '{}/fragdev/fragdev/templates'.format(WEBROOT)
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'fragdev',
    'images',
    'projects',
    'wiblog',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

