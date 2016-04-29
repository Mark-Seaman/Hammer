from django.core.management.base import BaseCommand

from tool.doc import doc_command
from tool.log import log_exception, log
from tool.server import server_command


class Command(BaseCommand):
    help = 'Runs scripts in the Django context'

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            cmd = options['script'][0]
            args = options['script'][1:]
            log('SCRIPTOR: %s %s' % (cmd,args))
            if cmd=='doc':
                doc_command(self, args)
            elif cmd=='data':
                self.stdout.write('Data command: %s' % options['script'])
            elif cmd=='help':
                self.help()
            elif cmd=='log':
                log_command(self, args)
            elif cmd=='server':
                server_command(self,args)
            else:
                self.stdout.write('**Scriptor Error**: unknown command %s' % options['script'])
                self.help()
        except:
            log_exception(self,options['script'])

    def help(self):
        self.stdout.write('''

            usage: x command 
            
            command:
                doc    # work with document files
                data   # work with database content
                help   # show command help
                log    # work with application log
        ''')

