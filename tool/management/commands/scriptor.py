import sys, traceback
from django.core.management.base import BaseCommand, CommandError
from logging import getLogger
from os.path import join

from tool.doc import doc_command
from hammer.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Runs scripts in the Django context'

    def add_arguments(self, parser):
        parser.add_argument('script', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            print(options)
            return
            cmd = options['script'][0]
            args = options['script'][1:]
            logger = getLogger(__name__)
            logger.warning('SCRIPTOR: %s %s' % (cmd,args))
            if cmd=='doc':
                doc_command(self, args)
            elif cmd=='data':
                self.stdout.write('Data command: %s' % options['script'])
            elif cmd=='log':
                log_read(self)
            elif cmd=='test':
                self.stdout.write('Test command: %s' % options['script'])
                throw_exception()
            else:
                self.stdout.write('**Scriptor Error**: unknown command %s' % options['script'])
        except:
            log_exception(self,options['script'])


def throw_exception():
    assert(False)


def log_exception(self,args):
    self.stdout.write('**Scriptor Exception**')
    self.stdout.write('exception: %s %s' % (args[0],args[1:]))
    self.stdout.write('traceback %s' % traceback.format_exc())
    logger = getLogger(__name__)
    logger.warning('SCRIPTOR: exception %s %s' % (args[0],args[1:]))
    logger.warning('SCRIPTOR: %s' % traceback.format_exc())


def log_json(response):
    if response.ok and response.json()['status'] == 'okay':
       pass
    else:
       logger.warning('%s' % response.json())


def log_read(self):
    path = join(BASE_DIR,'log','hammer.log')
    text = '\n'.join(open(path).read().split('\n')[-100:])
    self.stdout.write(text)

