from django.shortcuts import render
from django.http import HttpResponse
from os.path import join, exists
from os import listdir

from hammer.settings import BASE_DIR

def home(request):
    title = "World's Simplest App"
    text = '''
    This is the simplest Django app that is possible. All extra stuff has
    been stripped out. 
    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))


def format_doc(f):  
    if exists(f):
        return "<pre>%s</pre>" % open(f).read()


def doc(request, title):
    directory = join(BASE_DIR, 'doc')
    if exists(directory):
        text = 'Directory exists : %s' % ', '.join(listdir(directory))
        text += format_doc(join(directory,title))
    else:
        text = 'Directory missing'
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))
