# To Do

## Milestone:  Deployment 

Next most important overall objective

Action:
    attach stylesheet from HTML5up
    streamline command script execution

   

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

    interactive remote debug

* Python & Django setup

    standardize python setup
    manage pip libraries
    install with requirements.txt

---

## 2. Hosting

* ISP - Digital Ocean

    get starting code from remote server
    setup Gunicorn/Nginx for new code

* Domains

    select domain to host app
    point domain to floating IP

* Server image

* Deployment

    document Gunicorn setup

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

    reconcile todo.py in hammer and bin   
    document and automate server management
    scriptor tools: user, tasks, thot
    command scripts: app, data, src


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
    test commands (rt, ft, ut, pt)
 
* Functional test

    test groups: 
        Smoke, Python, Files, System, Django, Doc, Automation, Pages
    move to tests/*.py
    page tester (text and HTML compare)
       
* Unit test

    setup unit tests for Django code
    create unit test for notes
    philosophy (internal, isolated, stateless)

* Page test

    capture pages: / /ToDo.md
    compare page text with expected
    

---

# New Action Items

