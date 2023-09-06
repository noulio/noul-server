# flake8: noqa
from .common import *

env = environ.Env(
    DEBUG=(bool, True),
)

environ.Env.read_env(BASE_DIR / ".env.local")

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")
