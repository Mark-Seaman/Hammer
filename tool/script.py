from genericpath import exists
from subprocess import Popen, PIPE

from tool.log import log, log_exception


def pandoc_html(path):
    if exists('/usr/bin/pandoc'):
        pandoc = '/usr/bin/pandoc'
    elif exists('/usr/local/bin/pandoc'):
        pandoc = '/usr/local/bin/pandoc'
    else:
        pandoc = '/bin/echo'
    if exists(path):
        script = [pandoc, '-t', 'html', path]
        output = Popen(script, stdout=PIPE).stdout
        return output.read().decode(encoding='UTF-8')
    else:
        return ("Path NOT found,  %s" % path)


def render_doc_html(path):
    '''Render the HTML for the doc content'''
    try:
        log('render_doc_html', path)
        return pandoc_html(path)
    except:
        log_exception()


def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    log('shell_command', cmd)
    return Popen(cmd.split(), stdout=PIPE).stdout.read()

