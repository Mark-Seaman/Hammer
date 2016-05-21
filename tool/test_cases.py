from os import environ

from bin.shell import shell_command, file_tree_list, shell_lines
from tool.models import Test

#------------------------------------------------------------------------------------
# Test Cases

def doc_test():
    return shell_command('x doc list')

def doc_read_test():
    return shell_lines('x doc read', 1100,1200)

def pip_test():
    return shell_command ('pip list')

def version_test():
    return shell_command('git status')

def files_test():
    return '\n'.join(file_tree_list(environ['p']))

def functional_test():
    return shell_command('functional_tests.py')

def webapp_test():
    return shell_command('x app list')

def curl_test():
    return shell_command('curl -s http://159.203.152.201/app/App/App')

#------------------------------------------------------------------------------------
# Test Registry

test_cases = {
    'doc': doc_test,
    'doc-read': doc_read_test,
    'pip': pip_test,
    'version': version_test,
    'files': files_test,
    'functional': functional_test,
    #'webapp':webapp_test,
    'curl': curl_test,
}

#Test.objects.all().delete()
for t in test_cases:
    if not Test.objects.filter(name=t):
        Test.objects.create(name=t)


