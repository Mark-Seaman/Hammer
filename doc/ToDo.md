# To Do

## Milestone:  Deployment 

Next most important overall objective

Action:

    get push from remote server
    create process for updating Django to 1.9.4
    setup Gunicorn/Nginx for new code
    use one-click setup for Droplet at Digital Ocean
    document and automate server management
    move code to remote server
    clone Hammer repo on Digital Ocean
    deploy using git pull
    remote restart of server


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

* Development tools

    build PyCharm project
    interactive debug
    server run script
    server stop script

* Python & Django setup

    standardize python setup
    manage pip libraries
    install with requirements.txt

---

## 2. Hosting

* ISP - Digital Ocean

    convert existing app to Hammer

* Domains

    select domain to host app
    point domain to floating IP

* Server image

* Deployment

    execute as django user
    upgrade server Django 1.9.4
    setup ssh key on Droplet
    copy git repo on Digital Ocean
    debug git pull
    rework Gunicorn setup to reflect directory structure

---

## 3. App

* Django app structure

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

    scriptor help
    clone for command dispatch

* Data management

Command Scripts to create
    server
    app
    test
    user
    data

Commands to extent
    cmd
    doc
    log

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

    debug ft on macbook
    test pip list
    test groups: 
        Smoke, Python, Files, System, Django, Doc, Automation, Pages
    move to tests/*.py
    philosophy (integrated,live data,system)
    page tester (text and HTML compare)
       

* Unit test

    create unit test for notes
    philosophy (internal, isolated, stateless)

* Quick test

    micro test for inner dev loop
    
