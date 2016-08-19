
from os import environ, system
from os.path import join

from shell import banner, file_tree_list, read_file
from doc import doc_path, doc_pick


def seamanslog_command(options):
    if options:
        cmd = options[0]
        args = options[1:]
        if cmd=='edit':
            seamanslog_edit(args[0])
        elif cmd=='list':
            seamanslog_list(args)
        elif cmd=='pick':
            doc = doc_pick(['seamanslog'])
            print(open(doc_path(doc)).read())
            print('     -- '+doc.replace('.md',''))
        elif cmd=='show':
            seamanslog_show(args)
        else:
            seamanslog_help(args)
    else:
        seamanslog_help()


def seamanslog_doc_path(doc=None):
    if doc:
        return join(environ['p'], 'Documents', 'seamanslog', doc)
    else:
        return join(environ['p'], 'Documents', 'seamanslog')


def seamanslog_edit(doc):
    system('e '+seamanslog_doc_path(doc))


def seamanslog_help(args=None):
    print('''
        Seamans Log Command

        usage: x seamanslog COMMAND

        COMMAND:

            list - list the document files
            show - show the doc content
        ''')


def seamanslog_list(args):
    path = seamanslog_doc_path()
    for f in file_tree_list(path):
        print(f.replace(path+'/', ''))


def seamanslog_show(args):
    print('Xxx Show')
    path = seamanslog_doc_path()
    for f in file_tree_list(path):
        print(banner(f.replace(path+'/', '')))
        print(read_file(f))

    