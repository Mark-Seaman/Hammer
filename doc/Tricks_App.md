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


### Views/URLs/Templates

* URL routes for docs
* load pages from template
* build layout page for common look


### Data models

Define data model code in tool/models.py

Migrate the database to create new tables

    $ dj makemigrations
    $ dj migrate




