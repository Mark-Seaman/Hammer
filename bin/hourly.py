
from os import environ, system
from os.path import join

from shell import banner, file_tree_list, read_file


def hourly_command(options):
    #print('Hourly command %s' % options)
    if options:
        cmd = options[0]
        args = options[1:]
        if cmd=='edit':
            hourly_edit()
        elif cmd=='list':
            hourly_list(args)
        elif cmd=='run':
            hourly_run(args)
        elif cmd=='show':
            hourly_show()
        else:
            hourly_help(args)
    else:
        hourly_help()


def hourly_doc_path(doc=None):
    return join(environ['p'], 'bin', 'hourly.py')


def hourly_edit():
    system('e '+hourly_doc_path())


def hourly_help(args=None):
    print('''
        Hourly Command

        usage: x hourly COMMAND

        COMMAND:

            edit - edit the hourly task
            list - list the document files
            run  - run all the requested scripts
            show - show the doc content
        ''')


def hourly_list(args):
    #print('NO hourly tasks are currently configured')
    print('Send Spiritual Things email')
    print('Send my To Do List')
    print('Send queued email')
    print('git pull')
    

def hourly_run(args):
    def execute(cmd):
        print(cmd)
        system(cmd)

    execute('git pull')
    execute('x spiritual send')
    execute('x todo send-todo')
    execute('x send dispatch')
    execute('test-system')


def hourly_show():
    print('Hourly Show')
    path = hourly_doc_path()
    print(banner(path.replace(path+'/', '')))
    print(read_file(path))

    