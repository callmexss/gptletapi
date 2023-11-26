import os

from dotenv import load_dotenv

from .base import *  # noqa


load_dotenv()

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

allowed_hosts = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1")
ALLOWED_HOSTS = allowed_hosts.split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

cors_origins = os.getenv("CORS_ORIGIN_WHITELIST", "")
cors_allowed = os.getenv("CORS_ALLOWED_ORIGIN", "")
CORS_ORIGIN_WHITELIST = cors_origins.split(",") if cors_origins else []
CORS_ALLOWED_ORIGIN = cors_origins.split(",") if cors_origins else []
