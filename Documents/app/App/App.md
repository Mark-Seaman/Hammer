# Hammer Core - App

Application development notes


## Django App Structure of Source Code
        
Django Directory Structure

           .
        ├── bin
        ├── data
        ├── doc
        │   └── app
        │       ├── App
        │       ├── Data
        │       ├── Doc
        │       ├── Hosting
        │       ├── Project
        │       ├── Script
        │       └── Test
        ├── hammer
        ├── log
        ├── simple
        │   └── django_project
        ├── static
        │   └── identity
        │       ├── assets
        │       │   ├── css
        │       │   │   └── images
        │       │   ├── fonts
        │       │   ├── js
        │       │   └── sass
        │       │       ├── base
        │       │       ├── components
        │       │       ├── layout
        │       │       └── libs
        │       └── images
        ├── tasks
        │   ├── migrations
        │   └── templates
        ├── tool
        │   ├── management
        │   │   └── commands
        │   ├── migrations
        │   └── templates
        └── webapp
            ├── migrations
            └── templates
        
        39 directories


Django Source code files
        
        .
        ├── __init__.py
        ├── bin
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   ├── bash-alias
        │   ├── bash-django-profile
        │   ├── bashrc
        │   ├── bashrc-server
        │   ├── cmd.py
        │   ├── cmd.pyc
        │   ├── cptree
        │   ├── data.py
        │   ├── data.pyc
        │   ├── doc.py
        │   ├── doc.pyc
        │   ├── e
        │   ├── functional_tests.py
        │   ├── functional_tests.pyc
        │   ├── log.py
        │   ├── log.pyc
        │   ├── page_tests.py
        │   ├── path
        │   ├── pip-list
        │   ├── qt
        │   ├── rbg
        │   ├── remote_tests.py
        │   ├── server.py
        │   ├── server.pyc
        │   ├── setup-simple
        │   ├── shell.py
        │   ├── shell.pyc
        │   ├── todo.py
        │   ├── todo.pyc
        │   ├── tool.py
        │   ├── tool.pyc
        │   ├── vc
        │   ├── web.py
        │   ├── web.pyc
        │   ├── welcome
        │   ├── x
        │   └── x.py
        ├── data
        │   ├── dev-data.json
        │   └── hammer.db
        ├── Documents
        │   └── Application_Development_Notes
        │       ├── App
        │       │   ├── App.md
        │       │   ├── ToDo_App.md
        │       │   └── Tricks_App.md
        │       ├── Data
        │       │   ├── Data.md
        │       │   ├── ToDo_Data.md
        │       │   └── Tricks_Data.md
        │       ├── Doc
        │       │   ├── Doc.md
        │       │   ├── ToDo_Doc.md
        │       │   └── Tricks_Doc.md
        │       ├── Hosting
        │       │   ├── Hosting.md
        │       │   ├── ToDo_Hosting.md
        │       │   └── Tricks_Hosting.md
        │       ├── Project
        │       │   ├── EngineeringLog.md
        │       │   ├── Project.md
        │       │   ├── README.md
        │       │   ├── ToDo.md
        │       │   ├── ToDo_Project.md
        │       │   ├── Tricks.md
        │       │   └── Tricks_Project.md
        │       ├── Script
        │       │   ├── Script.md
        │       │   ├── ToDo_Script.md
        │       │   └── Tricks_Script.md
        │       └── Test
        │           ├── FunctionalTest.md
        │           ├── Test.md
        │           ├── ToDo_Test.md
        │           └── Tricks_Test.md
        ├── hammer
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   ├── settings.py
        │   ├── settings.pyc
        │   ├── urls.py
        │   ├── urls.pyc
        │   ├── wsgi.py
        │   └── wsgi.pyc
        ├── log
        │   ├── django.log
        │   └── hammer.log
        ├── manage.py
        ├── simple
        │   ├── django_project
        │   │   ├── __init__.py
        │   │   ├── __init__.pyc
        │   │   ├── settings.py
        │   │   ├── settings.pyc
        │   │   ├── wsgi.py
        │   │   └── wsgi.pyc
        │   └── manage.py
        ├── static
        │   ├── SWS_Globe_small.jpg
        │   ├── hammer.css
        │   ├── identity
        │   │   ├── LICENSE.txt
        │   │   ├── README.txt
        │   │   ├── assets
        │   │   │   ├── css
        │   │   │   ├── fonts
        │   │   │   ├── js
        │   │   │   └── sass
        │   │   ├── images
        │   │   └── index.html
        │   ├── task.css
        │   └── webapp.css
        ├── tasks
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   ├── admin.py
        │   ├── admin.pyc
        │   ├── apps.py
        │   ├── models.py
        │   ├── models.pyc
        │   ├── task.py
        │   ├── task.pyc
        │   ├── templates
        │   │   ├── task.html
        │   │   ├── task_delete.html
        │   │   ├── task_detail.html
        │   │   ├── task_edit.html
        │   │   └── task_layout.html
        │   ├── tests.py
        │   ├── urls.py
        │   ├── urls.pyc
        │   ├── views.py
        │   └── views.pyc
        ├── tool
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   ├── admin.py
        │   ├── admin.pyc
        │   ├── apps.py
        │   ├── log.py
        │   ├── log.pyc
        │   ├── management
        │   │   ├── __init__.py
        │   │   ├── __init__.pyc
        │   │   └── commands
        │   │       ├── __init__.py
        │   │       ├── __init__.pyc
        │   │       ├── scriptor.py
        │   │       └── scriptor.pyc
        │   ├── migrations
        │   │   ├── 0001_initial.py
        │   │   ├── 0001_initial.pyc
        │   │   ├── __init__.py
        │   │   └── __init__.pyc
        │   ├── models.py
        │   ├── models.pyc
        │   ├── templates
        │   │   ├── dir.html
        │   │   ├── doc.html
        │   │   └── layout.html
        │   ├── test_cases.py
        │   ├── test_cases.pyc
        │   ├── tests.py
        │   ├── tst.py
        │   ├── tst.pyc
        │   ├── views.py
        │   └── views.pyc
        └── webapp
            ├── __init__.py
            ├── __init__.pyc
            ├── admin.py
            ├── admin.pyc
            ├── app.py
            ├── app.pyc
            ├── apps.py
            ├── migrations
            ├── models.py
            ├── models.pyc
            ├── templates
            │   ├── webapp.html
            │   ├── webapp_delete.html
            │   ├── webapp_detail.html
            │   ├── webapp_doc.html
            │   ├── webapp_edit.html
            │   └── webapp_layout.html
            ├── tests.py
            ├── urls.py
            ├── urls.pyc
            ├── views.py
            └── views.pyc
        
        39 directories, 203 files


## Settings management

All of the interesting setup occurs in hammer/settings.py

Both manage.py and hammer/wsgi.py both point to the proper settings file.

The database connection string is not under version control for security
reasons. Instead these files are loaded from a local version of 
hammer/db.py. 

The db.py file senses which database connection to use depending on the
hostname of the server.

    db.py plug-in


## Views/URLs/Templates

    improve stylesheet
    create layout.html
    select additional stylesheet
    select initial data type - note
    build routes
    build views
    import bootstrap
    base layout


## Data models

    note - model code
    form input for editing

