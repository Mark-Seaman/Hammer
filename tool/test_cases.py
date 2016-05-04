from os import environ

from bin.shell import shell_command, file_tree_list
from tool.models import Test

#------------------------------------------------------------------------------------
# Test Cases

def pip_test():
    return shell_command ('pip list')


def version_test():
    return shell_command('git status')


def files_test():
    return '\n'.join(file_tree_list(environ['p']))


def functional_test():
    return shell_command('functional_tests.py')


#------------------------------------------------------------------------------------
# Test Registry

test_cases = {
    'pip_test': pip_test,
    'version_test': version_test,
    'files_test': files_test,
    'functional_test': functional_test,
}


for t in test_cases:
    if not Test.objects.filter(name=t):
        Test.objects.create(name=t)


