# coding: utf-8
from __future__ import unicode_literals

from django.db import connection
from django.core.management.base import BaseCommand

from ... import SEARCH_TABLES


class Command(BaseCommand):
    help = 'Update trigram table.'

    def handle(self, *args, **options):
        cursor = connection.cursor()

        for view in SEARCH_TABLES:
            cursor.execute("REFRESH MATERIALIZED VIEW {view_name};".format(view_name=view))