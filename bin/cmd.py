from shell import  file_path, file_list, line_count, read_file, shell_command
from log import log


def cmd_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    log('Cmd command output %s' % options)
    cmd = options[0]
    args = options[1:]
    if cmd=='edit':
        cmd_edit(args)
    elif cmd=='list':
        cmd_list()
    elif cmd=='length':
        cmd_length()
    elif cmd=='read':
        cmd_read(args)
    else:
        cmd_help()


def cmd_edit(args):
    path = file_path('bin', args[0]+'.py')
    print(shell_command('e %s' % path))
    

def cmd_help():
    print('''
        usage: x cmd command

        command:
            edit     # Edit a specific document file
            help     # Show the commands
            list     # List the available commands
            length   # Measure the lines in each doc
            read     # Show the text from all document

        ''')


def cmd_list():
    files = file_list('bin','.py')
    files = [f for f in files if f!='__init__.py']
    for f in files:
        print(f)


def cmd_length():
    files = file_list('bin','.py')
    files = [f for f in files if f!='__init__.py']
    for f in files:
        fp = file_path('bin', f)
        print('%s : %d' % (f, line_count(fp)))


def cmd_read(args):
    if args:
        path = file_path('bin', args[0]+'.py')
        text = read_file (path)
        print(text)
    else:
        files = file_list('bin','.py')
        files = [f for f in files if f!='__init__.py']
        for f in files:
            path = file_path('bin', f)
            text = read_file(path)
            print(text)


