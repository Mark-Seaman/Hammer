from os import environ
from platform import node

from bin.shell import shell, file_tree_list, shell_lines, check_lines
from tool.models import Test

#------------------------------------------------------------------------------------
# Test Cases

def doc_test():
    return shell('x doc list')

def doc_read_test():
    return shell_lines('x doc read', 20000,21000)

def pip_test():
    return shell ('pip list')

def version_test():
    return shell('git status')

def files_test():
    return '\n'.join(file_tree_list(environ['p']))

def files_count_test():
    files = file_tree_list(environ['p'])
    return check_lines('File Count:', '\n'.join(files), 5300, 5400)

def hostname_test():
    return 'Hostname: %s' % node()

def pandoc_test():
    return shell('pandoc -t html %s/Documents/app/Test/FunctionalTest.md' % environ['p'])

def functional_test():
    return shell('functional_tests.py')

def python_version_test():
    from sys import version_info
    return str(version_info)

def server_ip_test():
    return shell('x server ip')

def tst_test():
    return shell('x tst list')

def webapp_test():
    return shell('x app list')

def curl_test():
    return shell('curl -s http://159.203.152.201/app/App/App')

def remote_server_test():
    return shell('x server command bin/remote_tests.py')


#------------------------------------------------------------------------------------
# Test Registry

test_cases = {
    'curl': curl_test,
    'doc': doc_test,
    'doc-read': doc_read_test,
    'files': files_test,
    'files-count': files_count_test,
    'functional': functional_test,
    'hostname': hostname_test,
    'pandoc': pandoc_test,
    'pip': pip_test,
    'python-version': python_version_test,
    'remote': remote_server_test,
    'server-ip': server_ip_test,
    'tst': tst_test,
    'version': version_test,
    # 'webapp':webapp_test,
}

#Test.objects.all().delete()

for t in test_cases:
    if not Test.objects.filter(name=t):
        Test.objects.create(name=t)


