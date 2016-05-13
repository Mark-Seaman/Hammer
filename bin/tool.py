from shell import  file_path, file_list, line_count, read_file, shell_command


def tool_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    #self.stdout.write('tool command output %s' % options)
    tool = options[0]
    args = options[1:]
    if tool=='edit':
        tool_edit(args)
    elif tool=='list':
        tool_list()
    elif tool=='length':
        tool_length()
    elif tool=='read':
        tool_read(args)
    else:
        tool_help()


def tool_edit(args):
    path = file_path('tool', args[0]+'.py')
    print(shell_command('e %s' % path))
    

def tool_help(self):
    print('''
        usage: x tool command

        command:
            edit     # Edit a specific document file
            help     # Show the Documents commands
            list     # List the available documents
            length   # Measure the lines in each documents
            read     # Show the text from all documents

        ''')


def tool_list():
    files = file_list('tool','.py')
    files = [f for f in files if f!='__init__.py']
    for f in files:
        print(f)


def tool_length():
    files = file_list('tool','.py')
    files = [f for f in files if f!='__init__.py']
    for f in files:
        fp = file_path('tool', f)
        print('%s : %d' % (f, line_count(fp)))


def tool_read(args):
    if args:
        path = file_path('tool', args[0]+'.py')
        text = read_file (path)
        print(text)
    else:
        files = file_list('tool','.py')
        files = [f for f in files if f!='__init__.py']
        for f in files:
            path = file_path('tool', f)
            text = read_file(path)
            print(text)


