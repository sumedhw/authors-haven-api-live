from .base import *
from .base import env


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-)#nxzzzt)wk)b+cu4bd4erx$&1t4e9z_@!p=xneo#t13%-(ak%")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@authors-haven.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
