# Engineering Log

This log keeps track of the total amount of time that has been invested in the
project.   It also provides a detailed history of the work done on the project.

This log will be very useful in helping to plan similar project and cost
estimates.


## History

**Total Investment - 111:00**


Fri, 05-13 - 6

    build notes for Hammer Core
    build notes for Hammer Extension Apps
    debug MyBook Apps

Thu, 05-12 - 8

    create new git project
    create clone of Hammer for MyBook
    move in old code from existing MyBook project
    create project context
    successful deployment to Digital Ocean
    debugging of pandoc path
    simplified MyBook business logic
    debugging on new business logic
    move across MyBook stylesheet

Wed, 05-11 - 8

    theme & fonts for PyCharm
    update deployment of MyBook
    save current data
    destroy DB
    upgrade MyBook online to Django 1.9.4
    rebuild tables
    test & debug application settings
    debug Gunicorn configuration
    test deployment

Mon, 05-09 - 8

    create App Master web app
    create initial doc content files for App Master
    build out application structure
    5-views: list, detail, add, edit, delete
    clone generic app structure
    plug in custom CSS
    investigate setup of CSS logic

5-5-2016 - 6

    Implement task edit, add, and delete views
    Add task list and details views
    Debug setting of styles in CSS
    Build tasks app in django
    Debug edit, add, and delete views
    Create reusable views
    Full user experience for tasks
    Build project planning tool (7x7 tricks)

5-4-2016 - 8 

    Create view to list the tasks
    Build simplest possible view for tasks
    Build task command script
    Add tasks app to Hammer
    Build functional test under tst
    Extend application logic
    Improve CSS logic

5-3-2016 - 8 

    update project plan and documents
    build basic test runner
    create database entries for diff tests
    calculate test output differences from expected
    show all failing test results
    build data script for save, load, migrate
    restructure command aliases 
    approve current test output (using tlike)
    Develop data management scripts

5-2-2016 - 8 

    investigate stylesheets at HTML5UP
    hook up CSS and static assets
    create separate docs for each ToDo list (7 functional areas)
    build document display logic for new style
    create layout.html template
    automatic test for collecting pages
    simplify design of command scripts
    move to aliases from scripts

4-29-2016 - 6 

    create todo list tool
    move doc.py, cmd.py, tool.py server.py to bin
    scriptor help and command dispatch
    pass all functional tests
    convert server.py script
    create tool/log.py & bin/log.py
    
4-28-2016 - 8

    setup git on remote server
    debug setup of simple.py
    strip out extra files on remote server
    improve remote command context
    debug install of full app
    pass remote_tests.py
    deploy full app
    rename app from django_project to hammer
    create process for updating Django to 1.9.4


4-26-2016 - 8

    create remote_tests.py to test:
        hostname
        python and django version
        pip list
    test for pages on remote server
    build simplest app on Digital Ocean single-click install
    build PyCharm project
    setup PyCharm to work with Hammer
    setup git on remote server
    convert to deploy using git pull
    interactive local debug
    

4-25-2016 - 3

    repurpose existing Digital Ocean Droplet to Hammer host
    setup git repo and pandoc on Droplet
    reassign floating IP

4-22-2016 - 8

    create doc edit
    build cmd script
    refactor cmd & doc logic into shell
    create server script
    implement server commands (console, deploy, command)
    create Droplet at Digital Ocean
    setup rsync to server
    create command context on remote server
    pull code from Digital Ocean
    install git on remote server
    set up ssh keys on django user

4-21-2016 - 8

    Better feedback for Scriptor errors
    Refactor functional test code
    Extend scriptor to deal with logs
    raw document display
    test for pandoc
    URL routes for docs
    load pages from template
    format output using pandoc
    page tester
    build layout page for common look

4-16-2016 - 2

    Plan out project tasks and priorities

4-15-2016 - 8

    Conceive of this project
    Build the git repo (hosted at GitHub)
    Write project goals, functional requirements, engineering log
    Write READ ME
    Write Functional Test
    Write Engineering Log
    Clone repo
    Write To Do list
    create command context (bin/bashrc)
    setup path
    setup vc command
    create ft command
    test for correct python version
    setup virtualenv
    create basic Django app
    build tool installed app
    create management commands
    debug Scriptor
    implement doc commands
    build logging facility
