from os import environ
from os.path import join

from log import log
from shell import file_tree_list


def source_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    log('Cmd command output %s' % options)
    if not options:
        source_help()
    else:
        cmd = options[0]
        args = options[1:]
        if cmd=='diff':
            source_diff(args)
        elif cmd=='list':
            source_list(args)
        else:
            source_help()


def source_help():
    print('''
        usage: x source command

        command:
            diff     # Calculate difference from other source
            edit     # Edit a specific document file
            help     # Show the commands
            list     # List the available commands
            length   # Measure the lines in each doc
            read     # Show the text from all document

        ''')


def source_list(args):

    def collect_files(files, base, directory=None, filetype=None):
        return set(file_tree_list(join(base, directory), filetype))

    def relative_paths(base,files):
        return [f.replace(base+'/','') for f in sorted(files)]

    if args:
        base = args[0]
    else:
        base = environ['p']+'/'

    files = set()
    files |= collect_files(files, base, 'bin')
    files |= collect_files(files, base, '', '.py')
    files |= collect_files(files, base, '', '.html')
    files |= collect_files(files, base, '', '.css')
    files = [x for x in files if not x.endswith('.pyc')]

    for f in relative_paths(base, files):
        print(f)

    print('%d files ' % len(files))


def source_diff(args):
    print('source diff ', args)


