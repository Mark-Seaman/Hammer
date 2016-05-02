# Technical Tricks

A project is accomplished by applying standard solutions to common problems.


## App

### Django app structure

The Django application code is built on the following directory structure.

    bin     # Commands to work with project

    doc     # Markdown files for documents

    hammer  # Application settings

    log     # Log files
    static  # Static assets for web site

    tool    # Workbench app logic
    tool/management
    tool/management/commands
    tool/migrations
    tool/templates


### Setting management

Create a new django project

    $ dj startproject hammer
    $ dj startapp tool


### Simplest app

settings.py   - Build the smallest possible web app
-----------

from django.conf.urls import patterns, url
from django.http import HttpResponse

# Required Django Setup
SECRET_KEY = 'KDqYibgo1ZI4QIHOFInXmTy6wknXxWiii5DBal825FQgCXo5zA'
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'django_project.settings'

def home(request):
    title = "World's Simplest App"
    text = '''
    This is the simplest Django app that is possible. All extra stuff has
    been stripped out. Only essential code remains. Source code lives
    in <b>sparkler/old/simple_settings.py</b>.
    '''
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))

urlpatterns = patterns('',
    url(r'^$', home)
)



### Views/URLs/Templates

* URL routes for docs
* load pages from template
* build layout page for common look

