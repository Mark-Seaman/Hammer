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



### Database

Create the initial database (developer) -- Create a sqlite DB

    $ dj makemigrations
    $ dj migrate


Create data directory to save database backups

In settings.py file use a database that matches the hosting server

    # Database
    from platform import node
    if 'iMac' in node():    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3', 
                'NAME': 'data/hammer.db',  # Database file
                'USER': '',             # Not used with sqlite3.
                'PASSWORD': '',         # Not used with sqlite3.
                'HOST': '',             # Set to empty string for localhost. 
                'PORT': '',             # Set to empty string for default. 
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'django',
                'USER': 'django',
                'PASSWORD': 'vZIyCeHKwV',
                'HOST': 'localhost',
                'PORT': '',
            }
        }

Destroy the old database tables


    cat <<EOF  >data-drop-tables
    drop table auth_group cascade;
    drop table auth_group_permissions cascade;
    drop table auth_permission cascade;
    drop table auth_user cascade;
    drop table auth_user_groups  cascade;
    drop table auth_user_user_permissions cascade;
    drop table contact_contact cascade;
    drop table django_admin_log  cascade;
    drop table django_content_type  cascade;
    drop table django_migrations  cascade;
    drop table django_session  cascade;
EOF

    dj dbshell < data-drop-tables

    echo dj makemigrations
    echo dj migrate 


### Views/URLs/Templates

* URL routes for docs
* load pages from template
* build layout page for common look


### Data models

Define data model code in tool/models.py

Migrate the database to create new tables

    $ dj makemigrations
    $ dj migrate




