"""Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import environ
from django.core.management.utils import get_random_secret_key
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read environment variables from the environment and a .env file.
env = environ.Env(
    SECRET_KEY=(str, get_random_secret_key()),
    DJANGO_DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    CSRF_TRUSTED_ORIGINS=(list, []),
    DATABASE_URL=(str, "sqlite://?timeout=20"),
    EMAIL_URL=(str, "consolemail://"),
    CACHE_URL=(str, "locmemcache://"),
    ADMIN_URL=(str, "admin/"),
    INTERNAL_IPS=(list, []),
    TAILWIND_CLI_PATH=(str, "~/.local/bin"),
)
environ.Env.read_env(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/4.1/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG")

# A list of strings representing the host/domain names that this Django site can serve.
# https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# A list of IP addresses that are allowed to access the django debug toolbar.
# https://docs.djangoproject.com/en/4.2/ref/settings/#internal-ips
INTERNAL_IPS = env.list("ALLOWED_HOSTS")

# A list of trusted origins for unsafe requests (e.g. POST).
# https://docs.djangoproject.com/en/4.1/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

# Application definition
# https://docs.djangoproject.com/en/4.1/ref/settings/#installed-apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]

# Third-party apps
INSTALLED_APPS += [
    "django_browser_reload",
    "django_htmx",
    "django_tailwind_cli",
    "django_extensions",
]

# Our apps
INSTALLED_APPS += ["{{ project_name }}"]

# Middleware definitions
# https://docs.djangoproject.com/en/4.1/topics/http/middleware/
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

# A string representing the full Python import path to your root URLconf.
# https://docs.djangoproject.com/en/4.1/ref/settings/#root-urlconf
ROOT_URLCONF = "{{ project_name }}.urls"

# A list containing the settings for all template engines to be used with Django.
# https://docs.djangoproject.com/en/4.1/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.csrf",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
            ],
        },
    },
]

# The full Python path of the WSGI application object that Django’s built-in servers
# (e.g. runserver) will use.
# https://docs.djangoproject.com/en/4.1/ref/settings/#wsgi-application
WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {"default": env.db_url("DATABASE_URL")}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Password hashers
# https://docs.djangoproject.com/en/dev/topics/auth/passwords/
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en"
LANGUAGES = [
    ("en", _("English")),
    ("de", _("German")),
]
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (SCSS, CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# https://docs.djangoproject.com/en/4.1/ref/settings/#static-files
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = (str(BASE_DIR / "assets"),)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# User uploaded static files
# https://docs.djangoproject.com/en/4.1/ref/settings/#media-url
# https://docs.djangoproject.com/en/4.1/ref/settings/#media-root
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Email backend
# https://docs.djangoproject.com/en/4.1/ref/settings/#email-backend
# https://docs.djangoproject.com/en/4.1/topics/email/
EMAIL_CONFIG = env.email_url("EMAIL_URL")
vars().update(EMAIL_CONFIG)

# Caches
# https://docs.djangoproject.com/en/4.1/ref/settings/#caches
CACHES = {"default": env.cache_url("CACHE_URL")}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-rich Testrunner
# https://github.com/adamchainz/django-rich#django_richtestrichrunner
TEST_RUNNER = "django_rich.test.RichRunner"

# django-tailwind-cli settings
TAILWIND_CLI_PATH = env.str("TAILWIND_CLI_PATH")

# Our settings
ADMIN_URL = env("ADMIN_URL")
SITE_ID = 1
