# Technical Tricks

A project is accomplished by applying standard solutions to common problems.


## Database

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



### Data models

Define data model code in tool/models.py

Migrate the database to create new tables

    $ dj makemigrations
    $ dj migrate




