import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    subprocess.call(shlex.split("pkill celery"))
    subprocess.call(shlex.split("celery -A playlistor worker -l info -P gevent -c 50"))


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting celery worker with autoreload")
        autoreload.run_with_reloader(restart_celery)
