from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

USE_SQL_LITE = (os.environ.get('USE_SQL_LITE') == 'True')

if USE_SQL_LITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': '5432',
        }
    }



# DJANGO REST FRAMEWORK SETTINGS (Development)
REST_FRAMEWORK = {
    # Common
    "NON_FIELD_ERRORS_KEY" : "error",

    # Auth
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # Filter
    "DEFAULT_FILTER_BACKENDS": ['django_filters.rest_framework.DjangoFilterBackend'],
    'SEARCH_PARAM': 'q',

    # Throttle
    "DEFAULT_THROTTLE_RATES": {
        'anon': '10/hour',
        'user': '100/hour',
        'password_change_attempt': '5/day',
        'profile_update_attempt': '500/day',
        'admin_attempt':'100/hour',
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL GATEWAY SETUP
EMAIL_USE_TLS = True
EMAIL_PORT = 587 # 587/465
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')



# CORS SETTINGS
CORS_ORIGIN_ALLOW_ALL = True

