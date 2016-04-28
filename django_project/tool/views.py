from django.shortcuts import render
from django.http import HttpResponse
from os.path import join, exists
from os import listdir
from subprocess import Popen,PIPE

from django_project.settings import BASE_DIR


#----------------------
# Helpers

def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    return Popen(cmd.split(), stdout=PIPE).stdout.read()


def format_doc(f):  
    if exists(f):
        return shell_command('pandoc -t html %s' % f)


def file_list():
    directory = join(BASE_DIR, 'doc')
    if exists(directory):
        return listdir(directory)


#----------------------
# Views

def home(request):
    title = "Directory"
    files = file_list()
    return render(request, 'dir.html', { 'title': title, 'files': files } )


def doc(request, title):
    directory = join(BASE_DIR, 'doc')
    if exists(directory):
        text = 'Directory exists : %s' % ', '.join(listdir(directory))
        text += format_doc(join(directory,title))
    else:
        text = 'Directory missing'
    return render(request, 'doc.html', { 'title': title, 'text': text } )