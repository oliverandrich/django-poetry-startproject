# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file
# https://docs.gunicorn.org/en/stable/settings.html
# https://adamj.eu/tech/2021/12/29/set-up-a-gunicorn-configuration-file-and-test-it/
import multiprocessing

import environ

env = environ.Env(
    GUNICORN_WORKERS=(int, multiprocessing.cpu_count() * 2 + 1),
    GUNICORN_MAX_REQUESTS=(int, 1000),
    GUNICORN_MAX_REQUESTS_JITTER=(int, 50),
)

wsgi_app = "{{ project_name }}.wsgi"

log_file = "-"

max_requests = env.int("GUNICORN_MAX_REQUESTS")
max_requests_jitter = env.int("GUNICORN_MAX_REQUESTS_JITTER")

workers = env.int("GUNICORN_WORKERS")
worker_tmp_dir = "/dev/shm"  # noqa: S108

bind = "0.0.0.0:8000"
