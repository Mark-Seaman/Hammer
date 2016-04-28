#!/usr/bin/env python
# Test to be run on Digital Ocean Server


from os import environ
from os.path import join
from unittest import  main

from functional_tests import FunctionalTestCase
from shell import shell_command, read_file

class RemoteTest(FunctionalTestCase):

    def test_remote_server(self):
        self.assertIn('OK', 'Run server test - OK')

    def test_host(self):
        from platform import node
        self.assertIn('Hammer', node())

    def test_version_control(self):
        expected = "On branch master\nYour branch is up-to-date with 'origin/master'.\n\nnothing to commit, working directory clean\n"
        self.assertEqual(shell_command('git status'), expected)


class PythonTest(FunctionalTestCase):

    def test_python_version(self):
        from sys import version_info
        expected = "sys.version_info(major=2, minor=7, micro="
        self.assertIn(expected, str(version_info))

    def test_virtual_env(self):
        output = shell_command ('which python')
        expected = '/usr/bin/python\n'
        self.assertEqual(output,expected)

    def test_pip_list(self):
        path = join(environ['p'],'bin','pip-list')
        expected = read_file(path)
        output = shell_command('pip list')
        self.assertEqual(output, expected)


if __name__ == '__main__': 
    main()
