from .base import *
from decouple import config

DEBUG = True
SECRET_KEY = config("SECRET_KEY", default="dev-secret")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}