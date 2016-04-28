from os import environ, listdir
from os.path import join

from bin.shell import  file_path, file_list, line_count, read_file, shell_command


def cmd_command(self, options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    #self.stdout.write('Cmd command output %s' % options)
    cmd = options[0]
    args = options[1:]
    if cmd=='edit':
        cmd_edit(self, args)
    elif cmd=='list':
        cmd_list(self)
    elif cmd=='length':
        cmd_length(self)
    elif cmd=='read':
        cmd_read(self,args)
    else:
        cmd_help(self)


def cmd_edit(self, args):
    path = file_path('tool', args[0]+'.py')
    self.stdout.write(shell_command('e %s' % path))
    

def cmd_help(self):
    self.stdout.write('''
        usage: x cmd command

        command:
            edit     # Edit a specific document file
            help     # Show the doc commands
            list     # List the available documents
            length   # Measure the lines in each documents
            read     # Show the text from all documents

        ''')


def cmd_list(self):
    files = file_list('tool','.py')
    files = [f for f in files if f!='__init__.py']
    for f in files:
        self.stdout.write(f)


def cmd_length(self):
    files = file_list('tool','.py')
    files = [f for f in files if f!='__init__.py']
    for f in files:
        fp = file_path('tool', f)
        self.stdout.write('%s : %d' % (f, line_count(fp)))


def cmd_read(self, args):
    if args:
        path = file_path('tool', args[0]+'.py')
        text = read_file (path)
        self.stdout.write(text)
    else:
        files = file_list('tool','.py')
        files = [f for f in files if f!='__init__.py']
        for f in files:
            path = file_path('tool', f)
            text = read_file(path)
            self.stdout.write(text)


