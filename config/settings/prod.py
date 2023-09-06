# flake8: noqa
from .common import *

env = environ.Env(
    DEBUG=(bool, False),
)

environ.Env.read_env(BASE_DIR / ".env.prod")

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")
