# Hosting

A project is accomplished by applying standard solutions to common problems.
Here is a checklist for Hosting issues.


## How to Setup a Digital Ocean Server

Hosting a web app at Digital Ocean is quick and easy to setup.  Even if the
long-term intention is to host the app elsewhere then it may be useful to
setup an application stack at Digital Ocean.

It takes about one hour to setup and deploy an app using the automated scripts
and recipes for creating a simple Django app.


## Create a Droplet at Digital Ocean

    Selections:

        Django 14.04 in One-click Apps
        Size $5  - 512 MB Memory / 20 GB Disk / NYC3
        Add SSH Keys
        Hostname "Women2Women" ("W2W-Staging")

    Networking:

        Set Floating IP
        Domain - Set up domain

    Setup Console

        Set up floating IP to web app
        Record DJANGO_IP in bin/bashrc

    Point domain to floating IP


## Server Access 

    Configure SSH Key to Root

    Configure SSH Key to Django

    Copy SSH files to Django user .ssh


## Version control

    Install git on Digital Ocean server (Login as root)

        $ x server root
        $ git
        $ apt-get update
        $ apt-get install git
        $ git
        $ git status

    Clone repo

        $ server console
        $ git clone git@github.com:Shrinking-World/Hammer.git


## Configure Services

    Nginx  -- /etc/nginx/sites-enabled/django

        scp etc-nginx-sites-enabled-django root@$DJANGO_IP:/etc/nginx/sites-enabled/django
        ssh root@104.131.120.95 service nginx restart

    Gunicorn -- /etc/init/gunicorn.conf
        
        scp etc-init-gunicorn.conf root@$DJANGO_IP:/etc/init/gunicorn.conf
        ssh root@104.131.120.95 service gunicorn restart


## Deployment

    $ server deploy
    $ server restart
    $ server web

