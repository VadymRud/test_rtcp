from django.core.management.base import BaseCommand, CommandError
from testdbs.models import  Rtu, AiDesc, BiDesc


class Command(BaseCommand):
    help = 'Add data to db from csv file'

    def add_arguments(self, parser):
        parser.add_argument('filecsv', nargs='+', type=str)

    def handle(self, *args, **options):
        pass
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
