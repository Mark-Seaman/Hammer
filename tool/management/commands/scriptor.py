from django.core.management.base import BaseCommand

from tool.log import log_exception, log


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
            else:
                self.stdout.write('**Scriptor Error**: unknown command %s' % options['script'])
                self.help()
        except:
            log_exception(self,options['script'])

    def help(self):
        self.stdout.write('''

            usage: x command 
            
            command:
                data   # work with database content
                help   # show command help
        ''')

