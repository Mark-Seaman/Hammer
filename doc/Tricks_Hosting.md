# Technical Tricks

A project is accomplished by applying standard solutions to common problems.


## Hosting

### ISP - Digital Ocean

/etc/init/gunicorn.conf

    description "Gunicorn daemon for Django project"

    start on (local-filesystems and net-device-up IFACE=eth0)
    stop on runlevel [!12345]

    # If the process quits unexpectadly trigger a respawn
    respawn

    setuid django
    setgid django
    chdir /home/django

    exec gunicorn \
        --name=hammer \
        --pythonpath=hammer \
        --bind=127.0.0.1:9000 \
        --config /etc/gunicorn.d/gunicorn.py \
        hammer.wsgi:application

---

/etc/nginx/sites-enabled/django

    upstream app_server {
        server 127.0.0.1:9000 fail_timeout=0;
    }

    server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;

        root /usr/share/nginx/html;
        index index.html index.htm;

        client_max_body_size 4G;
        server_name _;

        keepalive_timeout 5;

        # Your Django project's media files - amend as required
        location /media  {
            alias /home/django/hammer/hammer/media;
        }

        # your Django project's static files - amend as required
        location /static {
            alias /home/django/hammer/static;
        }

        # Proxy the static assests for the Django Admin panel
        location /static/admin {
           alias /usr/lib/python2.7/dist-packages/django/contrib/admin/static/admin/;
        }

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass http://app_server;
        }
    }



### Domains


### Server image


### Deployment


### Version control

Install git on Digital Ocean server

    $ x server console
    $ git
    $ apt-get update
    $ apt-get install git
    $ git
    $ git status


