# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file
# https://docs.gunicorn.org/en/stable/settings.html
# https://adamj.eu/tech/2021/12/29/set-up-a-gunicorn-configuration-file-and-test-it/
import multiprocessing

from environs import Env

env = Env()

wsgi_app = "{{ project_name }}.wsgi"

log_file = "-"

max_requests = env.int("GUNICORN_MAX_REQUESTS", default=1000)
max_requests_jitter = env.int("GUNICORN_MAX_REQUESTS_JITTER", default=50)

workers = env.int("GUNICORN_WORKERS", default=multiprocessing.cpu_count() * 2 + 1)
worker_tmp_dir = "/dev/shm"  # noqa: S108

bind = env.str("GUNICORN_BIND", default="0.0.0.0:8000")
