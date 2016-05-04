#!/usr/bin/env python

from os import environ
from os.path import join
from platform import node
from unittest import TestCase, main

from shell import shell_command, read_file, file_tree_list



class FunctionalTestCase(TestCase):

    def assertLength(self, output, expected):
        '''Same length of arguments'''
        self.assertEqual(len(output), len(expected))

    def assertBetween(self, output, min, max):
        '''Check that value is within expected bounds'''
        self.assertLessEqual(output, max)
        self.assertGreaterEqual(output, min)

    def assertLines(self, output, min, max):
        '''Check that the number of lines is within bounds'''
        self.assertBetween(len(output.split('\n')), min, max)

    def assertFiles(self, path, min, max):
        '''Check that the number of lines is within bounds'''
        self.assertBetween(len(file_tree_list(path)), min, max)
    
    def assertShell(self, command, min, max):
        '''Check outline of a shell command; num lines is within bounds'''
        self.assertLines(shell_command(command), min, max)


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)


class PythonTest(FunctionalTestCase):

    def test_python_version(self):
        from sys import version_info
        expected = "sys.version_info(major=2, minor=7, micro="
        self.assertIn(expected, str(version_info))

    def test_virtual_env(self):
        output = shell_command ('which python')
        expected = environ['HOME']+'/Tools/env-python27/bin/python\n'
        self.assertEqual(output,expected)

    def test_pip_list(self):
        path = join(environ['p'],'bin','pip-list')
        expected = read_file(path)
        output = shell_command('pip list')
        self.assertEqual(output, expected)


class SystemTest(FunctionalTestCase):

    def test_file_count(self):
        files = file_tree_list(environ['p'])
        self.assertBetween(len(files), 160,180)

    def test_system_hostname(self):
        host = node()
        self.assertTrue ('iMac' in host or 'macbook' in host)

    def test_pandoc(self):
        self.assertShell('pandoc -v', 23,23)
        self.assertShell('pandoc -t html %s/doc/FunctionalTest.md' % environ['p'], 60,70)


class DjangoTest(FunctionalTestCase):

    def test_django_directory(self):
        self.assertFiles(join(environ['p'],'hammer'), 7,10)

    def test_tool_directory(self):
        self.assertFiles(join(environ['p'],'tool'), 30,35)

    def test_django_version(self):
        self.assertIn('Django (1.9.4)', shell_command('pip list'))


class ServerTest(FunctionalTestCase):

    def test_welcome(self):
        cmd = 'cat /home/django/hammer/bin/welcome'
        self.assertLines(shell_command('x server command '+cmd), 7,8)

    def test_hostname(self):
        self.assertIn('Hammer\n', shell_command('x server command hostname') )
      
    def test_ip(self):
        self.assertIn('159.203.152.201', shell_command('x server ip'))

    def test_remote_server(self):
        shell_command('x server command bin/remote_tests.py')

    def test_tst(self):
        self.assertShell('x tst list', 3,7)


class DocTest(FunctionalTestCase):

    def test_documents(self):
        self.assertLines(shell_command('x doc list'), 17, 25)

    def test_doc_length(self):
        self.assertLines(shell_command('x doc length'), 17,25)

    def test_doc_read(self):
        self.assertLines(shell_command('x doc read'), 850,900)

    def test_doc_help(self):
        self.assertLines(shell_command('x doc help'), 12,12)

    def test_todo_list(self):
        f = join(environ['p'], 'doc', 'ToDo.md')
        self.assertLines(open(f).read(), 50,70)

    def test_data(self):
        f = join(environ['p'], 'data', 'dev-data.json')
        self.assertLines(open(f).read(), 270,280)


class AutomationTest(FunctionalTestCase):

    def test_log(self):
        self.assertLines(shell_command('x log'), 7,50)

    def test_log_clear(self):
        self.assertEqual(shell_command('x log clear'), 'Logs cleared\n')

    def test_cmd_list(self):
        self.assertLines(shell_command('x cmd list'), 4,15)

    def test_cmd_length(self):
        self.assertLines(shell_command('x cmd length'), 4,15)

    def test_cmd_read(self):
        self.assertLines(shell_command('x cmd read'), 900,1000)

    def test_cmd_help(self):
        self.assertLines(shell_command('x cmd help'), 12,12)

    def test_script_help(self):
        self.assertLines(shell_command('x script help'), 9,12)


if __name__ == '__main__': 
    main()


