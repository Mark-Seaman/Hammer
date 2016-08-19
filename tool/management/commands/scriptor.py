from django.core.management.base import BaseCommand
import traceback

from bin.shell import banner
from tool.log import log_exception, log
from tool.page import page_command
from tool.project import project_command
from tool.tst import tst_command
from tasks.task import task_command
from thot.thot import thot_command


class Command(BaseCommand):
    help = 'Runs scripts in the Django context'

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            cmd = options['script'][0]
            args = options['script'][1:]
            log('SCRIPTOR: %s %s' % (cmd, args))
            if cmd=='app':
                webapp_command(self,args)
            elif cmd=='help':
                self.help()
            elif cmd=='page':
                page_command(self, args)
            elif cmd=='project':
                project_command(self,args)
            elif cmd=='task':
                task_command(self, args)
            elif cmd=='thot':
                thot_command(self, args)
            elif cmd=='tst':
                tst_command(self, args)
            else:
                self.stdout.write('**Scriptor Error**: unknown command %s' % options['script'])
                self.help()
        except:
            log_exception()
            self.stdout.write(banner('**Scriptor Exception**'))
            self.stdout.write('Scriptor Exception (%s %s)' % (cmd,args))
            self.stdout.write(traceback.format_exc())

    def help(self):
        self.stdout.write('''

            usage: x command 
            
            command:
                help   # show command help
                task   # work with tasks for user
                tst    # perform diff testing
        ''')

