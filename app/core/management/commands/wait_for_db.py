import time

from psycopg2 import OperationalError as Psycopg20Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20Error, OperationalError):
                self.stdout.write('database unavailable')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database available'))
