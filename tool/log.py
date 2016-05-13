import traceback
from logging import getLogger


def log(text, value=None):
    logger = getLogger(__name__)
    if value:
        logger.warning("%s: %s" % (text,value))
    else:
        logger.warning(text)


def log_page(page):
    log('Page: ', page)


def log_exception():
    logger = getLogger(__name__)
    logger.warning('SCRIPTOR: %s' % traceback.format_exc())


def log_json(response):
    if response.ok and response.json()['status'] == 'okay':
        pass
    else:
        logger = getLogger(__name__)
        logger.warning('%s' % response.json())
