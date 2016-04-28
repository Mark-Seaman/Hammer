# To Do

## Milestone:  Deployment 

Next most important overall objective


Done:
    build PyCharm project
    interactive local debug


Action:

   

---

## Project Objectives

* deployment on Digital Ocean
* data type driven development
* data management automation
* clonable project
* hammer test infrastructure
* use PyCharm to manage all project files


---

## 1. Project

* Directory structure

* Command context

* Version control

    setup git on remote server

* Development tools

    interactive remote debug
    command line runserver

* Python & Django setup

    create process for updating Django to 1.9.4
    standardize python setup
    manage pip libraries
    install with requirements.txt

---

## 2. Hosting

* ISP - Digital Ocean

    create one-click setup for Droplet at Digital Ocean
    get starting code from remote server
    setup Gunicorn/Nginx for new code

* Domains

    select domain to host app
    point domain to floating IP

* Server image

* Deployment

    upgrade server Django 1.9.4
    rework Gunicorn setup (move django_project to hammer)

---

## 3. App

* Django app structure

    convert existing app to Hammer
    decide on plug-in dj-apps (thot, tasks, docs, notes, time)

* Setting management

    git ignore db.py
    db.py plug-in

* Database

    recreate database with new code

* Views/URLs/Templates

    select initial data type - note
    build routes
    build views
    import bootstrap
    base layout

* Data models

    note - model code
    form input for editing

---

## 4. Script

* Scriptor

    move server.py to bin
    scriptor help
    clone for command dispatch
    document and automate server management

    scriptor
        doc
        user
        tasks,thot  (business logic)

    bin
        app
        cmd
        data
        log
        src
        server
        test (rt, ft, ut, pt)


* Data management


* Automation of data models

    load/save scenarios
    import/export scenarios

* Logging

    refactor logging code
    log(event_text)
    log_exception(event_text)
    log_history()

---

## 5. Doc

* Markdown documents

    write project plan (with estimated time to MVP)
        

* Display of formatted output

    setup pandoc (local and server)
    notes view

* Import/export

* Dynamic content editing

    generic view for editing using forms


---

## 6. Test

* Hammer test
    
    setup redis
    build scriptor test command
    manage expected results
    build approval command script
    enumerate tests

    
* Functional test

    test groups: 
        Smoke, Python, Files, System, Django, Doc, Automation, Pages
    move to tests/*.py
    page tester (text and HTML compare)
       

* Unit test

    create unit test for notes
    philosophy (internal, isolated, stateless)

* Quick test

    micro test for inner dev loop
    
