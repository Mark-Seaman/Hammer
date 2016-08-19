
from os import environ, system
from os.path import join

from shell import banner, file_tree_list, read_file

def client_command(options):
    if options:
        cmd = options[0]
        args = options[1:]
        if cmd=='edit':
            if args:
                client_edit(args[0])
            else:
                print('no file given')
        elif cmd=='history':
            client_history(args)
        elif cmd=='list':
            client_list(args)
        elif cmd=='show':
            client_show(args)
        else:
            client_help(args)
    else:
        client_help()


def client_doc_path(doc=None):
    path = join(environ['p'], 'Documents', 'tech', 'client')
    if doc:
        path = join(path, doc)
    return path


def client_edit(doc):
    system('e '+client_doc_path(doc))


def client_help(args=None):
    print('''
        Client Command

        usage: x client COMMAND

        COMMAND:

            history client - show the client history
            list - list the document files
            show - show the doc content
        ''')


def client_history(args=None):
    if args:
        doc = args[0]+'-Done'
        print('client history: %s-Done' % args[0])
        path = client_doc_path(doc)
        print(banner(doc.replace(path+'/', '')))
        print(read_file(path))
    else:
        print('no client given')


def client_list(args):
    path = client_doc_path()
    for f in file_tree_list(path):
        print(f.replace(path+'/', ''))


def client_show(args):
    print('Client Show')
    if args:
        doc = args[0]
        path = client_doc_path(doc)
        print(banner(doc.replace(path+'/', '')))
        print(read_file(path))
    else:
        path = client_doc_path()
        for f in file_tree_list(path):
            print(banner(f.replace(path+'/', '')))
            try:
                print(read_file(f))
            except:
                print('**Exception**: client_show %s' % f)

