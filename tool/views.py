from django.shortcuts import render
from django.http import HttpResponse
from os.path import join, exists
from os.path import isfile
from os import listdir
from subprocess import Popen,PIPE

from hammer.settings import BASE_DIR
from log import log

#----------------------
# Helpers

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
        if exists(path+'.md'):
            script = [pandoc, '-t', 'html', path+'.md']
            output = Popen(script, stdout=PIPE).stdout
            return output.read().decode(encoding='UTF-8')
        else:
            return ("Path NOT found,  %s.md" % path)
    except:
        log_exception()

# def format_doc(f):
#     log('format doc', f)
#     if exists(f):
#         return shell_command('pandoc -t html %s' % f)
#     else:
#         return '<h1>File is missing, %s</h1>' % f


def file_list():
    log('files')
    directory = join(BASE_DIR, 'Documents')
    if exists(directory):
        return listdir(directory)


#----------------------
# Views

def home(request):
    title = "Directory"
    files = file_list()
    return render(request, 'dir.html', { 'title': title, 'files': files } )


def doc(request, title):
    f = join(BASE_DIR, 'Documents', title)
    log('doc', f)
    # if exists(directory) and isfile(directory):
    #     #text = 'Directory exists : %s' % ', '.join(listdir(directory))
    #     #text = format_doc()
    #
    # else:
    #     text = 'Document file is missing, '
    text = render_doc_html(f)
    return render(request, 'doc.html', { 'title': title, 'text': text } )