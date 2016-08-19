#!/usr/bin/env python

from os import environ, system
from os.path import join
from sys import argv

from shell import shell, file_tree_list
from log import log
from switches import APP_DIR, APP_DIRS, APP_PORT


def app_path(topic=None):
    path = environ['p']
    if topic:
        path = join(path, topic)
    return path
    

def app_help():
    '''Show all the app apps and their usage.'''
    print('''
    usage:  app cmd [args]

    cmd:

        edit    file   - Edit the app
        kill           - Kill the local web server
        list    [file] - List all app source code files
        path    [file] - Lookup the path for the file
        run            - Run the local web server
        search  text   - Find text in the source code
        template [file] - Edit the template
            ''')


def kill_server():
    cmd = '''x=`ps -ef | grep -v grep | grep runserver | awk '{ print $2 }'`
        [ ! -z "$x" ]  && echo kill $x   && kill $x'''
    system(cmd)


def list_files():
    '''List the source code for the app'''
    files = []
    dirs = APP_DIRS
    for d in dirs:
        files += file_tree_list(app_path(d),'.py')
    files = [f.replace(app_path()+'/','') for f in files]
    print ('\n'.join(sorted(files)))


def run_server():
    system('''
            cd $p;
            echo python manage.py runserver %s;
            echo sleep 2
            echo x web http://127.0.0.1:%s/;
           ''' % (APP_PORT, APP_PORT))


def app_command(options):
    '''Execute all of the app specific apps'''
    log('app command output %s' % options)
    if options:
        cmd = options[0]
        args = options[1:]
         
        if cmd=='edit':
            shell('e %s' % app_path(APP_DIR+'/'+args[0]+'.py'))

        elif cmd=='kill':
            kill_server()

        elif cmd=='list':
            list_files()

        elif cmd=='path':
            print(app_path(args[0]))
        
        elif cmd=='run':
            run_server()

        elif cmd=='search':
            system('grep %s $p/*/*.py' % args[0])

        elif cmd=='template':
            shell('e %s' % app_path('templates/%s.html' % args[0]))

        else:
            print('No app command found, '+cmd)
            app_help()
    else:
        print('No arguments given')
        app_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    app_command(argv)

