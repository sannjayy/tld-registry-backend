from pathlib import Path
import os

ALLOWED_HOSTS = ['*']

# DATABASE
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

# DJANGO REST FRAMEWORK SETTINGS (PRODUCTION)
REST_FRAMEWORK = {
    # Common
    "NON_FIELD_ERRORS_KEY" : "error",

    # Auth
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # Disable Browsable API
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],

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

# CORS SETTINGS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # :TODO DELETE
    "http://127.0.0.1:3000", # :TODO DELETE
]

# SECURITY SETTINGS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    # { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    # { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# EMAIL GATEWAY SETUP
EMAIL_USE_TLS = True
EMAIL_PORT = 587 # 587/465
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')