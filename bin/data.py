from os import system, environ
from os.path import join

from log import log


def data_command(options):
    log('data command %s' % options)

    cmd = options[0]
    args = options[1:]
    if cmd=='save':
        data_save(args)
    elif cmd=='sql':
        data_sql(args)
    # elif cmd=='csv':
    #     data_csv()
    elif cmd=='read':
        data_read(args)
    elif cmd=='reset':
        data_reset()
    elif cmd=='migrate':
        data_migrate()
    elif cmd=='load':
        data_load(args)
    elif cmd=='count':
        data_count(args)
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
            reset     # Data reset
            save      # Save a copy of data as JSON
            help      # Show the valid commands

        ''')


def data_reset():
    from platform import node
    if 'iMac' in node() or 'macbook' in node():
        system ('rm $p/data/w2w.db')
    else:
        system('''
            cat <<EOF  | psql
                drop table auth_group cascade;
                drop table auth_group_permissions cascade;
                drop table auth_permission cascade;
                drop table auth_user cascade;
                drop table auth_user_groups cascade;
                drop table auth_user_user_permissions cascade;
                drop table django_admin_log cascade;
                drop table django_content_type cascade;
                drop table django_migrations cascade;
                drop table django_session cascade;
                drop table tool_test cascade;
                drop table tool_page cascade;
                drop table tool_project cascade;
EOF
            ''')


def data_read(args):
    f = join(environ['p'], 'data/%s-cases.csv' % data_server(args))
    system('x case read')


def data_server(args):
    if args and args[0]=='production':
        return 'production'
    elif args and args[0]=='staging':
        return 'staging'
    else:
        return 'dev'
#
#
# def data_csv():
#     f = '$p/data/production-w2w_case.csv'
#     system("echo 'copy w2w_case to stdout csv header;' | psql >"+f)


def data_sql(args):
    system("pg_dump > $p/data/%s-data.sql" % data_server(args))


def data_count(args):
    system('''
        wc -l $p/data/%s-data.json
        # cat $p/data/%s-data.json
        ''' % (data_server(args), data_server(args)))


def data_load(args):
    system ('''
        cd $p &&
       echo python ./manage.py loaddata  $p/data/%s-data.json
        ''' % data_server(args))


def data_migrate():
    system ('''
        cd $p
        python ./manage.py makemigrations
        python ./manage.py migrate
        ''')


def data_save(args):
    system ('''
        cd $p &&
        python ./manage.py dumpdata      | python -mjson.tool > $p/data/%s-data.json
        python ./manage.py dumpdata auth | python -mjson.tool > $p/data/%s-auth.json
        python ./manage.py dumpdata tool | python -mjson.tool > $p/data/%s-tool.json
        ''' % (data_server(args),data_server(args),data_server(args)))
