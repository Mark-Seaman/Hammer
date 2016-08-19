
from os import environ, system
from os.path import join

from shell import banner, file_tree_list, read_file
from doc import doc_pick, doc_path


def faceblog_command(options):
    print('faceblog command %s' % options)
    if options:
        cmd = options[0]
        args = options[1:]
        if cmd=='edit':
            faceblog_edit(args[0])
        elif cmd=='list':
            faceblog_list(args)
        elif cmd=='send':
            doc = doc_pick(['seamanslog'])
            faceblog_send(doc)
        elif cmd=='show':
            faceblog_show(args)
        else:
            faceblog_help(args)
    else:
        faceblog_help()


def faceblog_doc_path(doc=None):
    if doc:
        return join(environ['p'], 'Documents', 'seamanslog', doc)
    else:
        return join(environ['p'], 'Documents', 'seamanslog')


def faceblog_edit(doc):
    system('e '+faceblog_doc_path(doc))


def faceblog_help(args=None):
    print('''
        faceblog Command

        usage: x faceblog COMMAND

        COMMAND:

            list - list the document files
            send - post an article to facebook
            show - show the doc content
        ''')


def faceblog_list(args):
    print('faceblog list')
    path = faceblog_doc_path()
    for f in file_tree_list(path):
        print(f.replace(path+'/', ''))


def faceblog_send(doc):
    system('x send doc %s faceblog' % doc)
    system('x send dispatch')


def faceblog_show(args):
    print('faceblog Show')
    path = faceblog_doc_path()
    for f in file_tree_list(path):
        print(banner(f.replace(path+'/', '')))
        print(read_file(f))

    