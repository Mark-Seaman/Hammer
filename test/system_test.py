from platform import node
from os import environ
from os.path import join
from sys import version_info

from bin.shell import shell, file_tree_list, shell_lines, check_lines
from bin.shell import check_lines, shell, file_tree_list, match
from bin.switches import TEST_DOC


def system_disk_free_test ():
    df = shell('df /')
    used = df.split()[-2][:-1]
    if (int(used) > 65):   # Disk usage should be less than 65%
        print('Disk Free: %s percent (should be less than 65)\n%s' % (used, df))


def system_files_count_test():
    files = file_tree_list(environ['p'])
    return check_lines('File list', '\n'.join(files), 4400, 5600)


# def system_files_list_test():
#     return '\n'.join(file_tree_list(environ['p']))


def system_host_test():
    return 'Hostname: %s' % node()


def system_ip_test():
    return match('inet', shell('ifconfig'))


def system_pandoc_test():
    return shell('pandoc -t html %s' % TEST_DOC)


def system_pip_test():
    return shell('pip list')


def system_python_files_test():
    files = file_tree_list(environ['p'], '.py')
    if 'MyBook' in environ['p']:
        return check_lines('Python file list', '\n'.join(files), 90, 100)
    else:
        return check_lines('Python file list', '\n'.join(files), 58, 65)


def system_python_version_test():
    return str(version_info)


def system_python_virtualenv_test():
        return shell ('which python')


def system_html_files_test():
    files = file_tree_list(join(environ['p'], 'tool', 'templates'), '.html')
    return check_lines('HTML file list', '\n'.join(files), 11, 32)
    


