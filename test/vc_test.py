'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''


from bin.shell import  shell
from bin.switches import ON_INTERNET


def vc_status_test():
    '''Test the git status command'''
    return shell('git status')


def vc_pull_test():
    if ON_INTERNET:
        return shell('git pull')
