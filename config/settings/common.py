# flake8: noqa
import environ

from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]


# Internationalization

LANGUAGE_CODE = "ko-KR"

TIME_ZONE = "Asia/Seoul"


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "media/"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
