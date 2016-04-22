
#-----------------------------------------------------------------------------------------------------------------
# Command scripts

from os import environ, listdir
from os.path import join

from hammer.settings import BASE_DIR
from bin.shell import shell_command


def doc_command(self, options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    #self.stdout.write('Doc command output %s' % options)
    cmd = options[0]
    args = options[1:]
    if cmd=='edit':
        doc_edit(self, args)
    elif cmd=='list':
        doc_list(self)
    elif cmd=='length':
        doc_length(self)
    elif cmd=='read':
        doc_read(self)
    # elif cmd=='save':
    #     thot_save()
    # elif cmd=='load':
    #     thot_load()
    # elif cmd=='import':
    #     import_thots()
    # elif cmd=='export':
    #     export_thots()
    else:
        doc_help(self)


def doc_edit(self, args):
    path = join(environ['p'], 'doc', args[0])
    self.stdout.write(shell_command('e %s' % path))


def doc_help(self):
    self.stdout.write('''
        usage: x doc command

        command:
            edit     # Edit a specific document file
            help     # Show the doc commands
            list     # List the available documents
            length   # Measure the lines in each documents
            read     # Show the text from all documents

        ''')

def doc_dir(f=''):
    #if f:
        return join(BASE_DIR,'doc',f)
    # else:
    #     return join(BASE_DIR,'doc')

def doc_list(self):
    files = listdir(join(BASE_DIR,'doc'))
    for f in files:
        self.stdout.write(f)

def doc_length(self):
    
    files = listdir(doc_dir())
    for f in files:
        fp = doc_dir(f)
        lines = open(fp).read().split('\n')
        self.stdout.write('%s : %d' % (f,len(lines)))

def doc_read(self):
    path = join(BASE_DIR,'doc')
    files = listdir(doc_dir())
    for f in files:
        text = open(doc_dir(f)).read()
        self.stdout.write(text)
