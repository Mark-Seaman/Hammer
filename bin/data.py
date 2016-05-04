from os import system
from log import log


def data_command(options):
    log('data command %s' % options)

    cmd = options[0]
    args = options[1:]
    if cmd=='save':
        data_save()
    elif cmd=='migrate':
        data_migrate()
    elif cmd=='load':
        data_load()
    elif cmd=='count':
        data_count()
    else:
        data_help()

#----------------------------------------------------------------
# Commands


def data_help():
    print('''
        usage: x data command

        command:
            count     # Edit a specific document file
            load      # Load the data from JSON file
            migrate   # List the available documents
            save      # Save a copy of data as JSON
            help      # Show the valid commands

        ''')


def data_count():
    system('''
        wc -l $p/data/dev-data.json
        # cat $p/data/dev-data.json
        ''')


def data_load():
    system ('''
        cd $p &&
        python ./manage.py loaddata  $p/data/dev-data.json
        ''')


def data_migrate():
    system ('''
        cd $p &&
        python ./manage.py makemigrations
        python ./manage.py migrate
        ''')


def data_save():
    system ('''
        cd $p &&
        python ./manage.py dumpdata | python -mjson.tool > $p/data/dev-data.json
        ''')
