import os

from dotenv import load_dotenv

from .base import *  # noqa


load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'gptlet.app']
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