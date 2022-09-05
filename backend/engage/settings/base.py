"""
Django settings for engage project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from celery.schedules import crontab
from dotenv import load_dotenv

from engage.celery import app


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load the env file
# u should put the .env file in the main root dir (outside backend folder)
load_dotenv(os.path.join(f'{BASE_DIR.parent.parent}', '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)xyyk9-p5-w-jn^j)756w%&0dy4&i)w2vvoe^5_ui)t^5$x^v%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '172.19.224.1', 'dev.engageplaywin.com', '192.168.153.143','cms.engage.devapp.co']


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'captcha',
    'phonenumber_field',
    'rest_framework',
    'django_filters',
    'django_extensions',
    'drf_yasg',
    'ckeditor',
    'timezone_field',
    'celery',
    'django_celery_beat',
    'django_celery_results',
    'solo',
    'django_countries',
    'axes',
    'engage.account',
    'engage.operator',
    'engage.tournament',
    'engage.core',
    'django_password_validators',
    'django_password_validators.password_history',
]

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'engage.account.middlewares.LastSeenMiddleware',
    'axes.middleware.AxesMiddleware',
    'common.middleware.AccountExpiry',
    
]

# Block only on username
#AXES_ONLY_USER_FAILURES=True
AXES_FAILURE_LIMIT=3
AXES_COOLOFF_TIME=0.02 # 2 hours

ROOT_URLCONF = 'engage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'engage.operator.context_processors.region',
                'engage.operator.context_processors.operator',
                'engage.core.context_processors.profile_states',
                'engage.core.context_processors.date_picker',
                'engage.core.context_processors.notifications',
                'engage.core.context_processors.fcm_api_config',
            ],
            'libraries':  {
                'big_number': 'engage.core.templatetags.big_number',
            }
        },
    },
]

WSGI_APPLICATION = 'engage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
#    'default': {
#         'ENGINE':  'django.db.backends.postgresql_psycopg2',
#         'NAME': 'engage-dev',
#         'USER': 'mighty',
#         'PASSWORD': 'password',
#         'HOST': '10.153.104.178',
#         'PORT': '5432',
#     }
   'default': {
        'ENGINE':  'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'mighty',
        'PASSWORD': 'password',
        'HOST': '164.92.224.12',
        'PORT': '5432',
    }
#    'default': {
#         'ENGINE':  'django.db.backends.postgresql_psycopg2',
#         'NAME': 'engage_dev',
#         'USER': 'mighty',
#         'PASSWORD': 'password',
#         'HOST': '164.92.224.12',
#         'PORT': '5432',
#     }
}

# AUTH Model

AUTH_USER_MODEL = 'account.User'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django_password_validators.password_history.password_validation.UniquePasswordsValidator',
        'OPTIONS': {
             # How many recently entered passwords matter.
             # Passwords out of range are deleted.
             # Default: 0 - All passwords entered by the user. All password hashes are stored.
            'last_passwords': 5 # Only the last 5 passwords entered by the user
        }
    },
    {   'NAME': 'engage.account.validator.CustomPasswordValidator',

},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# from django.utils.translation import gettext_lazy as _


# LANGUAGES = [
#     ('en-us', _('English')),
# ]

# LOCALE_PATHS = ( "/xxx/xxx/Projects/xxx/sites/avb/locale/",)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / '..' / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = '/static/'


MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

NGINX_GAMES_REDIRECT_PATH = '/html5games/' # this defined inside the nginx config
GAMES_URL = BASE_DIR / 'games/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cache

REDIS_HOST = os.getenv('BROKER_HOST', 'redis')
REDIS_PORT = os.getenv('BROKER_PORT', '6379')
BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': BROKER_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
}

# Celery

CELERY_TASK_TRACK_STARTED = True
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

app.conf.beat_schedule = {
    'check_active_matches_winners': {
        'task': 'engage.tournament.tasks.check_active_matches_winners',
        'schedule': crontab(minute='*/1'),
    },
    'how_to_use_notification': {
      'task': 'engage.account.schedulers.how_to_use_notification',
      'schedule': crontab(hour=12)
    },
    # 'active_days_notification': {
    #     'task': 'engage.account.schedulers.active_days_notification',
    #     'schedule': crontab(minute=0, hour=0)
    # },
    'check_users_level': {
        'task': 'engage.account.schedulers.check_users_level',
        'schedule': crontab(minute=0, hour=0)
    },
    'happy_birthday_notification': {
        'task': 'engage.account.schedulers.happy_birthday_notification',
        'schedule': crontab(hour=0, minute=10)
    },
    'once_a_month_notification': {
        'task': 'engage.account.schedulers.once_a_month_notification',
        'schedule': crontab(0, 0, day_of_month='1')
    },
    'daily_event_check_notification': {
        'task': 'engage.account.schedulers.daily_event_check_notification',
        'schedule': crontab(minute=0, hour='*/8')
    },
    'every_14_days_notifications': {
        'task': 'engage.account.schedulers.every_14_days_notifications',
        'schedule': crontab(minute=0, hour=4)
    }
}


# CURRENCY

CURRENCIES = ('USD',)


# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
    ],
    'EXCEPTION_HANDLER': 'common.exceptions.custom_exception_handler'
}

API_VERSION = 'v1'


# CKEditor

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strikethrough', 'Undo', 'Redo'],
            ['NumberedList', 'BulletedList', 'Outdent'],
            ['Link', 'Unlink', 'Anchor', 'Image'],
            ['TextColor', 'BackgroundColor', 'RemoveFormat', 'Source'],
            ['Smiley']
        ]
    }
}


# Django JET

JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
    {'label': 'General', 'app_label': 'core', 'items': [
        {'name': 'core.configuration'},
        {'name': 'core.sticker'},
        {'name': 'core.trophy'},
        {'name': 'core.event'},
        {'name': 'core.featuredgame'},
        {'name': 'core.mission'},
        {'name': 'core.battlepass'},
        {'name': 'core.notifications'},
    ]},
    {'label': 'Users', 'items': [
        {'name': 'account.user','label': 'CMS Users','url': '/admin/account/staffuser/','permissions': ['account.user']} ,
        {'name': 'account.user','label': 'Engage Subscribers','url': '/admin/account/enduser/','permissions': ['account.user']},
        {'name': 'auth.group'},
    ]},
    {'label': 'Tournaments', 'items': [
        {'name': 'core.game'},
        {'name': 'core.html5game'},
        {'name': 'tournament.tournament'},
    ]},
    {'label': 'Operators', 'items': [
        {'name': 'operator.region'},
        {'name': 'operator.operator'},
        {'name': 'operator.operatorad'}
    ]},
]

# JET
X_FRAME_OPTIONS = 'SAMEORIGIN'
JET_SIDE_MENU_COMPACT = True
# JET_INDEX_DASHBOARD = 'engage.dashboard.CustomDashboard'
JET_APP_INDEX_DASHBOARD = None
JET_CHANGE_FORM_SIBLING_LINKS = True


# FCM PUSH NOTIFICATION
FCM_SERVER_KEY = os.getenv('FCM_SERVER_KEY', 'KEY')
FCM_CONFIG = {
    'apiKey': os.getenv('FCM_API_KEY'),
    'authDomain': os.getenv('FCM_AUTH_DOMAIN'),
    'projectId': os.getenv('FCM_PROJECT_ID'),
    'storageBucket': os.getenv('FCM_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FCM_SENDER_ID'),
    'appId': os.getenv('FCM_APP_ID'),
    'measurementId': os.getenv('FCM_MEASUREMENT_ID'),
}

# Regions
REGION_COOKIE_NAME = 'region'

#Captcha
RECAPTCHA_PUBLIC_KEY = '6LfgQHkgAAAAALOSa2gHJKxSLSINgKWNKrEF2d7O'
RECAPTCHA_PRIVATE_KEY = '6LfgQHkgAAAAABqHnQmpqbvfwo2TgiXY_L0LIT00'
RECAPTCHA_REQUIRED_SCORE = 0.5

#Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp-mail.outlook.com'  # SMTP Server
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # sender email
EMAIL_PORT = 25  # Server port
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # gmail app password
EMAIL_USE_TLS = True  # _SSL?

# Session Expiration
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Set to True to end session when browser is closed


PASS_EXPIRE_DAYS = 14
# SESSION_COOKIE_AGE = 60 * 60  # in seconds this is equal to 60 minutes
# SESSION_SAVE_EVERY_REQUEST = True  # Overhead ?
CUSTOM_COOKIE_AGE = 60 * 60  # in seconds this is equal to 60 minutes
CUSTOM_COOKIE_RENEW = True

AXES_ONLY_USER_FAILURES = True
AXES_META_PRECEDENCE_ORDER = ('HTTP_X_FORWARDED_FOR', 'X_FORWARDED_FOR', 'REMOTE_ADDR') # should fix ip issue needs testing 'HTTP_X_REAL_IP', 'HTTP_X_FORWARDED_FOR', 'X_FORWARDED_FOR', 'REMOTE_ADDR'
# AXES_PROXY_COUNT = 1
AXES_ENABLE_ACCESS_FAILURE_LOG = True
AXES_LOCKOUT_CALLABLE = "engage.account.views.lockout"
AXES_ONLY_ADMIN_SITE = True
AXES_ENABLE_ADMIN = False
# CORS_ORIGIN_WHITELIST=('example.net')
API_SERVER_URL='http://192.168.153.62:8099'