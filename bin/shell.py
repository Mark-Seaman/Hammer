from os import environ, listdir, system, walk
from os.path import join, exists
from platform import node
from subprocess import Popen,PIPE


def shell_lines(cmd, min=0, max=10):
    lines = shell_command(cmd).split('\n')
    if len(lines) < min or len(lines)> max:
        message = '%s is %d (should be between %d and %d'
        return (message % (cmd, len(lines), min, max))


def read_file(path):
    '''Read a file and return the text'''
    if not exists(path):
        return 'Error:  File not found %s' % path
    return open(path).read()


def line_count(path):
    '''Read a file and count the lines of text'''
    return len(read_file(path).split('\n'))


def file_tree_list(path):
    '''Return a list of files in the directory tree'''
    files = []
    for root, dirnames, filenames in walk(path):
        if not '.git' in root: 
            for filename in filenames:
                files.append(join(root, filename))
    return files


def file_list(path, filetype=None):
    '''Return a list of files in the directory'''
    files =  listdir(file_path(path))
    if filetype:
        files = [ f for f in files if f.endswith(filetype) ]
    return files


def file_path (d=None, f=None):
    path = join(environ['p'],d)
    if f:
        return join(path, f)
    return path


def differences(answer,correct):
    '''   Calculate the diff of two strings   '''
    if answer!=correct:
        t1 = '/tmp/diff1'
        t2 = '/tmp/diff2'
        with open(t1,'wt') as file1:
            #print (answer)
            file1.write(str(answer)+'\n')
        with open(t2,'wt') as file2:
            file2.write(str(correct)+'\n')
        diffs = shell_command('diff %s %s' %(t1, t2))
        if diffs:
            #print('Differences detected:     < actual     > expected')
            #print (diffs)
            return diffs


def hostname():
    return node()


def banner(name):
    '''Show a banner for this file in the output'''
    return '\n%s\n%s%s\n%s\n' % ('-'*80, ' '*30, name,'-'*80)


def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    text = Popen(cmd.split(), stdout=PIPE).stdout.read()
    text = str(text)
    #text = unicode(text)
    text.decode('utf-8', 'ignore')
    return text 


def shell_command_script(cmd):
    '''Execute a shell command and return stdout'''
    return Popen(cmd, stdout=PIPE).stdout.read()


