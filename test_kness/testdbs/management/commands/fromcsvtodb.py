import csv
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.apps import apps
from testdbs.models import Rtu, AiDesc, BiDesc
from pprint import pprint


def get_model_by_db_table(db_table):
    for model in apps.get_models():
        if model._meta.db_table == db_table:
            return model
    else:
        # here you can do fallback logic if no model with db_table found
        raise ValueError('No model found with db_table {}!'.format(db_table))
        # or return None


def fromfilecsv(filename):
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            return your_list
    except Exception as e:
        print("Error {}".format(e))

class Command(BaseCommand):
    help = 'Add data to db from csv file'

    def add_arguments(self, parser):
        parser.add_argument('filecsv', nargs='+', type=str)

    def handle(self, *args, **options):
        if 'rtu' in options['filecsv']:
            try:
                app_model = get_model_by_db_table('rtu')
                pprint(app_model.objects.all())
                data = fromfilecsv(options['filecsv'][1])
                pprint(data[1:])
                for cell in data[1:]:
                    line = cell[0].split(';')
                    app_model.objects.create(url=line[1], time_upd_int=line[2])
            except Exception as e:
                print("Error {}".format(e))
        # # for poll_id in options['poll_ids']:
        # #     try:
        # #         poll = Poll.objects.get(pk=poll_id)
        # #     except Poll.DoesNotExist:
        # #         raise CommandError('Poll "%s" does not exist' % poll_id)
        # #
        # #     poll.opened = False
        # #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
