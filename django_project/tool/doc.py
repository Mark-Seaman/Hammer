
#-----------------------------------------------------------------------------------------------------------------
# Command scripts

from os import environ, listdir
from os.path import join

from django_project.settings import BASE_DIR
from bin.shell import  file_path, file_list, line_count, read_file, shell_command


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
    path = file_path('doc', args[0]+'.md')
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


def doc_list(self):
    files = file_list('doc','.md')
    for f in files:
        self.stdout.write(f)


def doc_length(self):
    files = file_list('doc','.md')
    for f in files:
        fp = file_path('doc', f)
        self.stdout.write('%s : %d' % (f, line_count(fp)))


def doc_read(self):
    files = file_list('doc','.md')
    for f in files:
        path = file_path('doc', f)
        text = read_file(path)
        self.stdout.write(text)
