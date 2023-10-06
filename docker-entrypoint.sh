#!/usr/bin/env bash

# https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
set -euxo pipefail

echo "Migrate database..."
python manage.py migrate

echo "Start gunicorn..."
gunicorn
