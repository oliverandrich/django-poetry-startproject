# django-poetry-startproject

![Screenshot of the landing page](docs/landingpage.png)

> Django startproject template with some poetry.

I took the inspiration from Jeff Triplett's [django-startproject](https://github.com/jefftriplett/django-startproject) and created my own starter for a fresh django project. It includes the batteries I use regularly. 🤷‍♂️

The template is also inspired by Carlton Gibson's Post [The Single Folder Django Project Layout](https://noumenal.es/notes/django/single-folder-layout/). It uses the single folder layout as a start as I always run in the same situation Carlton describes in his post. If you have to split the project into several apps, you can always call `python manage.py startapp` later on.

Out of the box SQLite is configured, but you can easily activate MySQL or Postgres support by following the steps add the end of this file.

## Features

- Django 4.2.x
- django-browser-reload
- django-environ
- django-htmx
- django-tailwind-cli
- whitenoise
- SQLite setup with WAL mode enabled (See `config/__init__.py`.)
- [Argon2 password hashing is activated](https://docs.djangoproject.com/en/4.1/topics/auth/passwords/)
- Local install of htmx.
- uses the [single folder Django project layout](https://noumenal.es/notes/django/single-folder-layout/)

### Development tools

- django-types
- model-bakery
- pytest
- pytest-cov
- pytest-django
- pytest-mock
- pre-commit setup inspired by [Boost your Django DX](https://adamchainz.gumroad.com/l/byddx)
- sane ruff configuration
- syrupy for snapshot testing

## Install

```shell
django-admin startproject \
    --extension=ini,py,toml,yaml,yml \
    --template=https://github.com/oliverandrich/django-poetry-startproject/archive/main.zip \
    example_project

# Setup environment
cd example_project
echo "DJANGO_DEBUG=True" >> .env

# Install dependencies
poetry install

# Migrate database
poetry run ./manage.py migrate

# Start dev server
poetry run ./manage.py tailwind runserver

# Or if you prefer django-extensions runserver_plus
poetry run ./manage.py tailwind runserver_plus

```

### Add Postgres support

```shell
cd example_project
poetry add psycopg2-binary
```

Set the environment variable DATABASE_URL to [something reasonable](https://django-environ.readthedocs.io/en/latest/types.html#environ-env-db-url)

### Add MySQL support

```shell
cd example_project
poetry add mysqlclient django-mysql
```

Follow the [installation instructions](https://django-mysql.readthedocs.io/en/latest/installation.html#id1) of `django-mysql` and set the environment variable DATABASE_URL to [something reasonable](https://django-environ.readthedocs.io/en/latest/types.html#environ-env-db-url)

## Environemt Variables for Docker

Or when run as a [12-Factor application](https://12factor.net).

| Environment Variable         | Default                   | Location                       |
| ---------------------------- | ------------------------- | ------------------------------ |
| SECRET_KEY                   | `get_random_secret_key()` | {{ project_name }}/settings.py |
| DJANGO_DEBUG                 | False                     | {{ project_name }}/settings.py |
| ALLOWED_HOSTS                | []                        | {{ project_name }}/settings.py |
| CSRF_TRUSTED_ORIGINS         | []                        | {{ project_name }}/settings.py |
| DATABASE_URL                 | "sqlite://?timeout=20"    | {{ project_name }}/settings.py |
| EMAIL_URL                    | "consolemail://"          | {{ project_name }}/settings.py |
| CACHE_URL                    | "locmemcache://"          | {{ project_name }}/settings.py |
| ADMIN_URL                    | "admin/"                  | {{ project_name }}/settings.py |
| INTERNAL_IPS                 | []                        | {{ project_name }}/settings.py |
| TAILWIND_CLI_PATH            | "~/.local/bin"            | {{ project_name }}/settings.py |
| GUNICORN_WORKERS             | "~/.local/bin"            | gunicorn.conf.py               |
| GUNICORN_MAX_REQUESTS        | 1000                      | gunicorn.conf.py               |
| GUNICORN_MAX_REQUESTS_JITTER | 50                        | gunicorn.conf.py               |

## Docker and docker-compose

The `Dockerfile` uses a multi stage process to embracing caching for building the container images.

## Contributing

Contributions, issues and feature requests are welcome!
Feel free to check [issues page](https://github.com/oliverandrich/django-poetry-startproject/issues).
