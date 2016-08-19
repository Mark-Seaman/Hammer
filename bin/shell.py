from os import environ, listdir, walk
from os.path import join, exists
from platform import node
from subprocess import Popen, PIPE


def match(word, text):
    return '\n'.join([x for x in text.split('\n') if word in x])


def exclude(word, text):
    return '\n'.join([x for x in text.split('\n') if not word in x])


def line_count(path):
    '''Read a file and count the lines of text'''
    return len(read_file(path).split('\n'))


def limit_lines(shell_command, min=None, max=None):
    '''Limit the lines to a certain number or echo all the output'''
    text = shell (shell_command)
    violation = check_lines(shell_command, text, min, max)
    if violation:
        text = text.split('\n')
        text = '\n'.join([line[:60] for line in text])
        #return violation+'\n'+text
        return violation
    return ''


def check_lines(label, lines, min=0, max=10):
    lines = lines.split('\n')
    if len(lines) < min or len(lines) > max:
        message = 'shell(%s) --> %d lines (should be between %d and %d)'
        return (message % (label, len(lines), min, max))


def shell_lines(cmd, min=0, max=10):
    return check_lines(cmd, shell(cmd), min, max)
    

def read_file(path):
    '''Read a file and return the text'''
    if not exists(path):
        return 'Error:  File not found %s' % path
    try:
        return open(path).read().decode(encoding='UTF-8')
    except:
        return '**error**: Bad file read, %s' % path


def line_count(path):
    '''Read a file and count the lines of text'''
    return len(read_file(path).split('\n'))


def filter_types(files, filetype=None):
    if filetype:
        files = [f for f in files if f.endswith(filetype)]
    return files


def file_tree_list(path, filetype=None):
    '''Return a list of files in the directory tree'''
    files = []
    for root, dirnames, filenames in walk(path):
        if not '.git' in root:
            for filename in filenames:
                files.append(join(root, filename))
    return filter_types(files, filetype)


def file_list(path, filetype=None):
    '''Return a list of files in the directory'''
    files = listdir(file_path(path))
    if filetype:
        files = [f for f in files if f.endswith(filetype)]
    return files


def file_path(d=None, f=None):
    path = d
    if f:
        return join(path, f)
    return path


def differences(answer, correct):
    '''   Calculate the diff of two strings   '''
    if answer != correct:
        t1 = '/tmp/diff1'
        t2 = '/tmp/diff2'
        with open(t1, 'wt') as file1:
            # print (answer)
            file1.write(str(answer) + '\n')
        with open(t2, 'wt') as file2:
            file2.write(str(correct) + '\n')
        diffs = shell('diff %s %s' % (t1, t2))
        if diffs:
            # print('Differences detected:     < actual     > expected')
            # print (diffs)
            return diffs


def hostname():
    return node()


def banner(name):
    '''Show a banner for this file in the output'''
    return '\n%s\n%s%s\n%s\n' % ('-' * 80, ' ' * 30, name, '-' * 80)


def shell(cmd):
    '''Execute a shell command and return stdout'''
    text = Popen(cmd.split(), stdout=PIPE).stdout.read()
    return text.decode(encoding='UTF-8')


def shell_command_script(cmd):
    '''Execute a shell command and return stdout'''
    return Popen(cmd, stdout=PIPE).stdout.read()
