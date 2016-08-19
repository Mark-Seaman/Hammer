from os import environ, system
from os.path import join

from shell import banner, file_tree_list, read_file, shell


def collab_command(options):
    print('Collab command %s' % options)
    cmd = options[0]
    args = options[1:]
    if cmd=='edit':
        collab_edit(args[0])
    if cmd=='list':
        collab_list(args)
    elif cmd=='show':
        collab_show(args)
    elif cmd=='web':
        collab_web(args)
    else:
        collab_help(args)


def collab_doc_path(doc=None):
    path = join(environ['p'], 'Documents', 'tech', 'collab')
    if doc:
        path = join(path, doc)
    return path


def collab_edit(doc):
    system('e '+collab_doc_path(doc))


def collab_help(args):
    print('''
        Collaboration Command

        usage: x collab COMMAND

        COMMAND:

            list - list the document files
            show - show the doc content
            web  - show the web page
        ''')


def collab_list(args):
    print('Collab list')
    path = collab_doc_path()
    for f in file_tree_list(path):
        print(f.replace(path+'/', ''))


def collab_show(args):
    print('Collaboration Show')
    path = collab_doc_path()
    for f in file_tree_list(path):
        print (f)
        print(banner(f.replace(path+'/', '')))
        try:
            print(read_file(f))
        except:
            print('**Exception**: collab_show %s' % f)


def collab_web(args):
    if not args:
        shell('x web http://seaman-tech.com/tech/collab')
    else:
        shell('x web http://seaman-tech.com/tech/collab/%s' % args[0])

