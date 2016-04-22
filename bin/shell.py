from os import environ, listdir, system, walk
from os.path import join, exists
from platform import node
from subprocess import Popen,PIPE


def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    return Popen(cmd.split(), stdout=PIPE).stdout.read()


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
                files.append(filename)
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


def hostname():
    return node()