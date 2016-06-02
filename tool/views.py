from django.shortcuts import render
from os import listdir
from os.path import isfile, isdir
from os.path import join, exists

from hammer.settings import BASE_DIR
from log import log
from tool.script import render_doc_html


def doc(request, title='/'):
    f = join(BASE_DIR, 'Documents', title)
    log('doc', f)
    if exists(f) and isdir(f):
        text = 'Directory exists : %s' % ', '.join(listdir(f))
        files = [x.replace('.md', '') for x in listdir(f)]
        return render(request, 'dir.html', {'title': title, 'text': text, 'dir': title, 'files': files})
    if exists(f) and isfile(f):
        return render_doc(request, f, title)
    if exists(f+'.md') and isfile(f+'.md'):
        return render_doc(request, f+'.md', title)
    else:
        return render_doc(request, f, title)


def render_doc(request, f, title):
    text = render_doc_html(f)
    return render(request, 'doc.html', {'title': title, 'text': text})
