from django.shortcuts import render
from os.path import join, exists
from os.path import isfile, isdir
from os import listdir
from subprocess import Popen, PIPE

from hammer.settings import BASE_DIR
from log import log


def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    log('shell', cmd)
    return Popen(cmd.split(), stdout=PIPE).stdout.read()


def render_doc_html(path):
    '''Render the HTML for the doc content'''
    try:
        log('render doc', path)
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
    except:
        log_exception()
#
#
# def file_list():
#     log('files')
#     directory = join(BASE_DIR, 'Documents')
#     if exists(directory):
#         return listdir(directory)
#


def home(request):
    title = "Directory"
    files = file_list()
    return render(request, 'dir.html', {'title': title, 'files': files})


def doc(request, title):
    f = join(BASE_DIR, 'Documents', title)
    log('doc', f)
    if exists(f) and isdir(f):
        text = 'Directory exists : %s' % ', '.join(listdir(f))
        files = [x.replace('.md', '') for x in listdir(f)]
        return render(request, 'dir.html', {'title': title, 'text': text, 'dir': title, 'files': files})
    elif exists(f) and isfile(f):
        text = render_doc_html(f)
        return render(request, 'doc.html', {'title': title, 'text': text})
    elif exists(f+'.md') and isfile(f+'.md'):
        text = render_doc_html(f+'.md')
        return render(request, 'doc.html', {'title': title, 'text': text})
    else:
        text = 'Document file is missing, ' + f
        return render(request, 'doc.html', {'title': title, 'text': text})
