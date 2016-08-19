import traceback
from datetime import datetime
from logging import getLogger
from os import remove
from os.path import join, dirname

from bin.files import read_text, list_files
from hammer.settings import LOG_DIR


def log(text, value=None):
    logger = getLogger(__name__)
    if value:
        text = "%s: %s" % (text,value)
    logger.warning(str(datetime.now())+',  '+text)


def log_exception():
    logger = getLogger(__name__)
    logger.warning('SCRIPTOR: %s' % traceback.format_exc())


def log_json(response):
    if response.ok and response.json()['status'] == 'okay':
        pass
    else:
        logger = getLogger(__name__)
        logger.warning('%s' % response.json())


def log_file():
    return join(LOG_DIR, 'hammer.log')


def append_log(doc, filename='page'):
    log(str(datetime.now())+',  '+doc)

#
# def log_page_old(request, title=None):
#     if not request or request.user.is_anonymous():
#          append_log('Anonymous '+str(title))
#     else:
#          append_log(request.user.username+' '+str(title))


def show_log():
    return read_text(log_file())


def list_logs():
    log = show_log()
    print len(log.split('\n')), log_file()


def clear_logs():
    d = join(dirname(BASE_DIR), 'logs')
    for f in list_files(d):
        f = f.replace('.log','')
        print 'remove', log_file(f)
        remove(log_file(f))