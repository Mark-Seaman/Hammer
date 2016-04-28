import sys, traceback
from django.core.management.base import BaseCommand, CommandError
from logging import getLogger
from os.path import join

from django_project.settings import BASE_DIR

def log_command(self, options):
    '''
    Execute a log command script from scriptor.  
    Parse off command and args and dispatch it.
    '''
    #self.stdout.write('Log command output %s' % options)
    if options[:]:

        cmd = options[0]
        args = options[1:]
        if cmd=='clear':
            log_clear(self)
    else:
        log_read(self)


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


def log_clear(self):
    path = join(BASE_DIR,'log','hammer.log')
    text = open(path, 'w').write('')
    self.stdout.write('Logs cleared')


def log_read(self):
    path = join(BASE_DIR,'log','hammer.log')
    text = '\n'.join(open(path).read().split('\n')[-100:])
    self.stdout.write(text)

