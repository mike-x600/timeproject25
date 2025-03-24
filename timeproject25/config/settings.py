import os
import sys
from .environment import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR + '/apps' )

def rel(*path):
    """
    Used to get the relative path for any file, combines with the BASEDIR
    @param path: the relative path for the file
    @return: absolute path to the file
    """
    return os.path.join(BASE_DIR, *path)

SECRET_KEY = env.str(
    "TIMEPROJECT25_SECRET_KEY", default="temp"
)

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "rest_framework",
    # "rest_framework.authtoken",
    # "allauth",
    # "allauth.account",
    # "allauth.socialaccount",
    # "dj_rest_auth",
    # "dj_rest_auth.registration",
    # "django_extensions",
    "django_filters",

    "drf_spectacular",
    "drf_spectacular_sidecar",
    # "drf_psq",
    # "corsheaders",
    "django_celery_beat",
    "django_celery_results",
    # our apps
    "core",
    "timeproject25",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "timeproject25.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DEBUG = True
DEBUG = False

ALLOWED_HOSTS = [
    env.str(
        "TIMEPROJECT25_ALLOWED_HOST",
        "localhost"
    )
]

# Static and media files
STATIC_URL = env.str(
    "TIMEPROJECT25_STATIC_URL",
    default="static/",
)
STATIC_ROOT = rel("static")
STATICFILES_DIR = rel("static")

# Media config
MEDIA_URL = "/media/"
MEDIA_ROOT = rel("media")

# AUTH_USER_MODEL = "accounts.User"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".NumericPasswordValidator"
        ),
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

SECURE_BROWSER_XSS_FILTER = env.bool(
    "TIMEPROJECT25_SECURE_BROWSER_XSS_FILTER",
    default=True,
)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "TIMEPROJECT25_SECURE_CONTENT_TYPE_NOSNIFF",
    default=True,
)
SESSION_COOKIE_HTTPONLY = env.bool(
    "TIMEPROJECT25_SESSION_COOKIE_HTTPONLY",
    default=True,
)
SESSION_COOKIE_SECURE = env.bool(
    "TIMEPROJECT25_SESSION_COOKIE_SECURE",
    default=True,
)
CSRF_COOKIE_SECURE = env.bool(
    "TIMEPROJECT25_CSRF_COOKIE_SECURE",
    default=True,
)
X_FRAME_OPTIONS = env.str(
    "TIMEPROJECT25_X_FRAME_OPTIONS",
    default="SAMEORIGIN",
)
SECURE_HSTS_SECONDS = env.int(
    "TIMEPROJECT25_SECURE_HSTS_SECONDS",
    default=31536000,
)  # 1 year
SESSION_COOKIE_NAME = "s"
CSRF_COOKIE_NAME = "c"

SITE_ID = env.int("SITE_ID", default=1)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = True

ANNON_RATE = env.int(
    "TIMEPROJECT25_ANNON_THROTTLE_RATE_PER_MIUTE",
    default=50,
)
USER_RATE = env.int(
    "TIMEPROJECT25_USER_THROTTLE_RATE_PER_MIUTE",
    default=100,
)

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        # Set throttling rates here
        "anon": f"{ANNON_RATE}/minute",
        "user": f"{USER_RATE}/minute",
    },
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Rest and all auth configurations
REST_AUTH_SERIALIZERS = {
    # Add custom serializers for Rest Auth
    "LOGIN_SERIALIZER": (
        "apps.accounts.serializers.CustomLoginSerializer"
    ),
    "TOKEN_SERIALIZER": (
        "apps.accounts.serializers.CustomTokenSerializer"
    ),
    "PASSWORD_RESET_SERIALIZER": (
        "apps.accounts.serializers"
        + ".CustomPasswordResetSerializer"
    ),
    "PASSWORD_RESET_CONFIRM_SERIALIZER": (
        "apps.accounts.serializers"
        + ".CustomPasswordResetConfirmSerializer"
    ),
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "apps.accounts.serializers.CustomRegisterSerializer"
}

# Frontend URL to be used for password reset email, needs to be
# of the form: <url>/<uid>/<token>, we will add the uid and token
PASSWORD_RESET_URL = env.str(
    "TIMEPROJECT25_PASSWORD_RESET_URL",
    "http://localhost:3000/",
)

# Frontend URL to be used for email verification
EMAIL_VERIFICATION_URL = env.str(
    "TIMEPROJECT25_EMAIL_VERIFICATION_URL",
    None
)

# Override the account adapter to use the custom one
ACCOUNT_ADAPTER = "apps.accounts.allauth_adapter.CustomAllauthAdapter"

# Mandate the need for an Email Address when registering.
ACCOUNT_EMAIL_REQUIRED = True

# Choose whether to use Email or Username to login.
# Omit to set as 'username'
ACCOUNT_AUTHENTICATION_METHOD = "email"

# Choose if user is logged out after changing password
LOGOUT_ON_PASSWORD_CHANGE = env.bool(
    "TIMEPROJECT25_LOGOUT_ON_PASSWORD_CHANGE",
    default=True,
)

# Choose the username field. None if not using username.
# Omit setting if using the default 'username' field.
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# Choose whether a username is required during registration.
# Omit setting if using the default 'username' field.
ACCOUNT_USERNAME_REQUIRED = False

# Choose whether old password needs to be entered when changing password
OLD_PASSWORD_FIELD_ENABLED = env.bool(
    "TIMEPROJECT25_OLD_PASSWORD_ENABLED",
    default=True,
)

# Choose whether email verification is required before login is allowed.
# Other options are: 'optional' , 'mandatory'
ACCOUNT_EMAIL_VERIFICATION = env.str(
    "TIMEPROJECT25_EMAIL_VERIFICATION",
    default="none",
)

# Celery configurations
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
# CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_BACKEND = env.str(
    "TIMEPROJECT25_CELERY_RESULT_BACKEND",
    "redis://localhost:6379/0", # redis://:password@host:port/db
)
CELERY_CACHE_BACKEND = "default"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = env.str(
    "TIMEPROJECT25_CELERY_BROKER_URL",
    "redis://localhost:6379/0", # redis://:password@host:port/db
)
CELERY_BROKER_CONNECTION_MAX_RETRIES = 10
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Swagger settings
SPECTACULAR_SETTINGS = {
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    
    'TITLE': 'Timeproject25 API',
    'DESCRIPTION': 'Useful tools for timetable management',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# Custom configs and settings
# Max page size for pagination, required since we are using dynamic page
# size pagination
MAX_PAGE_SIZE = env.int("MAX_PAGE_SIZE", 30)

# Url prefixes and settings
API_PREFIX = env.str(
    "TIMEPROJECT25_API_PREFIX", "api"
)
API_VERSION = env.str(
    "TIMEPROJECT25_API_VERSION", "v1"
)
PLATFORM_PREFIX = env.str(
    "TIMEPROJECT25_PLATFORM_PREFIX",
    "_platform",
)
DOCS_PREFIX = env.str(
    "TIMEPROJECT25_DOCS_PREFIX", "docs"
)

# Other settings
COMMUNICATOR_NAME = env.str(
    "TIMEPROJECT25_MAIL_COMMUNICATOR_NAME",
    "Admin",
)

# For the docs
CONTACT_EMAIL = env.str(
    "TIMEPROJECT25_CONTACT_EMAIL",
    "test@test.com",
)
SAMPLE_AUTH_TOKEN = env.str(
    "TIMEPROJECT25_SAMPLE_AUTH_TOKEN",
    "sjdhskjh3454343",
)
HOSTED_DOMAIN = env.str(
    "TIMEPROJECT25_HOSTED_DOMAIN",
    "https://ohuru.tech/",
)

ASGI_APPLICATION = "timeproject25.config.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env.str("DB_HOST", "localhost"),
        "USER": env.str("DB_USER", "postgres"),
        "NAME": env.str("DB_NAME", "timeproject"),
        "PASSWORD": env.str("DB_PASSWORD", "postgres"),
        "PORT": env.str("DB_PORT", "5432"), 
        "OPTIONS": {},
    }
}

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.environ.get('REDIS_URL', ('127.0.0.1', 6379))],
        },
    },
}