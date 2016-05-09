from django.core.management.base import BaseCommand
import traceback

from tool.log import log_exception, log
from tool.tst import tst_command
from tasks.task import task_command
from webapp.app import webapp_command


class Command(BaseCommand):
    help = 'Runs scripts in the Django context'

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            cmd = options['script'][0]
            args = options['script'][1:]
            log('SCRIPTOR: %s %s' % (cmd,args))
            if cmd=='app':
                webapp_command(self,args)
            elif cmd=='help':
                self.help()
            elif cmd=='task':
                task_command(self, args)
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
                help   # show command help
                task   # work with tasks for user
                tst    # perform diff testing
        ''')

