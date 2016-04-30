import traceback
from logging import getLogger


def log(text):
    logger = getLogger(__name__)
    logger.warning(text)


def log_exception(self):
    self.stdout.write('**Scriptor Exception**')
    self.stdout.write('traceback %s' % traceback.format_exc())
    logger = getLogger(__name__)
    logger.warning('SCRIPTOR: %s' % traceback.format_exc())


def log_json(response):
    if response.ok and response.json()['status'] == 'okay':
       pass
    else:
       logger = getLogger(__name__)
       logger.warning('%s' % response.json())
