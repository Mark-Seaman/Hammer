from os import environ, listdir
from os.path import join

from shell import  file_path, file_list, line_count, read_file, shell_command


def doc_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    #self.stdout.write('doc command output %s' % options)
    doc = options[0]
    args = options[1:]
    if doc=='edit':
        doc_edit(args)
    elif doc=='list':
        doc_list()
    elif doc=='length':
        doc_length()
    elif doc=='read':
        doc_read(args)
    else:
        doc_help()


def doc_edit(args):
    path = file_path('doc', args[0]+'.md')
    print(shell_command('e %s' % path))
    

def doc_help():
    print('''
        usage: x doc command

        command:
            edit     # Edit a specific document file
            help     # Show the doc commands
            list     # List the available documents
            length   # Measure the lines in each documents
            read     # Show the text from all documents

        ''')


def doc_list():
    files = file_list('doc','.md')
    for f in files:
        print(f)


def doc_length():
    files = file_list('doc','.md')
    for f in files:
        fp = file_path('doc', f)
        print('%s : %d' % (f, line_count(fp)))


def doc_read(args):
    if args:
        path = file_path('doc', args[0]+'.md')
        text = read_file (path)
        print(text)
    else:
        files = file_list('doc','.md')
        for f in files:
            path = file_path('doc', f)
            text = read_file(path)
            print(text)


