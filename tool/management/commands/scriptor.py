from django.core.management.base import BaseCommand
import traceback

from tool.log import log_exception, log
from tool.tst import tst_command


class Command(BaseCommand):
    help = 'Runs scripts in the Django context'

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            cmd = options['script'][0]
            args = options['script'][1:]
            log('SCRIPTOR: %s %s' % (cmd,args))
            if cmd=='data':
                self.stdout.write('Data command: %s' % options['script'])
            elif cmd=='help':
                self.help()
            elif cmd=='tst':
                tst_command(self, args)
            else:
                self.stdout.write('**Scriptor Error**: unknown command %s' % options['script'])
                self.help()
        except:
            log_exception(self)
            self.stdout.write('**Scriptor Exception**:  %s' % traceback.format_exc())

    def help(self):
        self.stdout.write('''

            usage: x command 
            
            command:
                data   # work with database content
                help   # show command help
                tst    # perform diff testing
        ''')

