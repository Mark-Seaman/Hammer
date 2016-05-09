# Functional Tests and Requirements

The project is controlled by functional tests.  These begin as a list of items
to do, but end an automated test script to exercise all product functionality.

The requirements are defined to address many different areas of functionality.
Acceptance of the product must be based on the testing of each area.


## Project

* Directory structure
* Command context
* Version control
* Development tools
* Python Virtualenv

    Plan out project tasks and priorities
    Conceive of this project
    Build the git repo (hosted at GitHub)
    Write project goals, functional requirements, engineering log
    Write READ ME
    Write Functional Test
    Write Engineering Log
    Clone repo
    Write To Do list

---

## Hosting

* ISP - Digital Ocean
* Domains
* Server image
* Deployment

    create Droplet at Digital Ocean
    setup rsync to server
    create command context on remote server
    pull code from Digital Ocean
    install git on remote server
    set up ssh keys on django user
    repurpose existing Digital Ocean Droplet to Hammer host
    reassign floating IP
    build simplest app on Digital Ocean single-click install
    improve remote command context
    debug install of full app
    pass remote_tests.py
    deploy full app
    rename app from django_project to hammer
    create process for updating Django to 1.9.4
    strip out extra files on remote server
    debug setup of simple.py
    setup git on remote server

---

## App

* Django app structure
* Setting management
* Views/URLs/Templates
* Style
* JavaScript

    create basic Django app
    build tool installed app
    investigate stylesheets at HTML5UP
    hook up CSS and static assets
    build document display logic for new style
    create layout.html template

---

## Data

* Database
* Data models
* Data management

---

## Doc

* Markdown documents
* Display of formatted output
* Import/export
* Dynamic content editing

    implement doc commands
    URL routes for docs
    load pages from template
    format output using pandoc
    create separate docs for each ToDo list (7 functional areas)
    create todo list tool

---

## Script

* Scriptor
* Automation of data models
* Logging

    create command context (bin/bashrc)
    setup path
    setup vc command
    create ft command
    test for correct python version
    setup virtualenv
    create management commands
    debug Scriptor
    build logging facility
    create doc edit
    build cmd script
    refactor cmd & doc logic into shell
    create server script
    implement server commands (console, deploy, command)
    setup git repo and pandoc on Droplet
    build PyCharm project
    setup PyCharm to work with Hammer
    setup git on remote server
    convert to deploy using git pull
    interactive local debug
    simplify design of command scripts
    move to aliases from scripts
    move doc.py, cmd.py, tool.py server.py to bin
    scriptor help and command dispatch
    convert server.py script
    create tool/log.py & bin/log.py

---

## Test

* Hammer test
* Functional test
* Unit test
* Quick test

    Better feedback for Scriptor errors
    Refactor functional test code
    Extend scriptor to deal with logs
    raw document display
    test for pandoc
    page tester
    build layout page for common look
    create remote_tests.py to test:
        hostname
        python and django version
        pip list
    test for pages on remote server
    automatic test for collecting pages
    pass all functional tests

