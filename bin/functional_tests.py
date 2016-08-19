#!/usr/bin/env python

from os import environ
from os.path import join
from platform import node
from unittest import TestCase, main

from shell import shell, read_file, file_tree_list



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
        self.assertLines(shell(command), min, max)


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)


class PythonTest(FunctionalTestCase):

    def test_python_version(self):
        from sys import version_info
        expected = "sys.version_info(major=2, minor=7, micro="
        self.assertIn(expected, str(version_info))

    def test_virtual_env(self):
        output = shell ('which python')
        expected = environ['HOME']+'/Tools/env-python27/bin/python\n'
        self.assertEqual(output,expected)


class DjangoTest(FunctionalTestCase):

    def test_django_directory(self):
        self.assertFiles(join(environ['p'],'hammer'), 7,10)

    def test_tool_directory(self):
        self.assertFiles(join(environ['p'],'tool'), 29,40)

    def test_django_version(self):
        self.assertIn('Django (1.9.4)', shell('pip list'))


class ServerTest(FunctionalTestCase):

    def test_welcome(self):
        cmd = 'cat /home/django/MyBook/bin/welcome'
        self.assertLines(shell('x server command ' + cmd), 7, 8)

    def test_hostname(self):
        self.assertIn('MyBookOnline.org', shell('x server command hostname'))
      
    def test_ip(self):
        self.assertIn('45.55.50.13', shell('x server ip'))


class DocTest(FunctionalTestCase):

    # def test_documents(self):
    #     self.assertLines(shell('x doc list'), 25, 30)
    #
    # def test_doc_length(self):
    #     self.assertLines(shell('x doc length'), 390,410)

    # def test_doc_read(self):
    #     self.assertLines(shell('x doc read'), 850,940)

    def test_doc_help(self):
        self.assertLines(shell('x doc help'), 12, 12)

    def test_todo_list(self):
        f = join(environ['p'], 'Documents', 'app', 'Project', 'ToDo.md')
        self.assertLines(open(f).read(), 50,120)

    def test_data(self):
        f = join(environ['p'], 'data', 'dev-data.json')
        self.assertLines(open(f).read(), 370,400)


class AutomationTest(FunctionalTestCase):

    def test_log(self):
        self.assertLines(shell('x log'), 7, 50)

    def test_log_clear(self):
        self.assertEqual(shell('x log clear'), 'Logs cleared\n')

    def test_cmd_list(self):
        self.assertLines(shell('x cmd list'), 4, 15)

    def test_cmd_length(self):
        self.assertLines(shell('x cmd length'), 4, 15)

    def test_cmd_read(self):
        self.assertLines(shell('x cmd read'), 900, 1300)

    def test_cmd_help(self):
        self.assertLines(shell('x cmd help'), 12, 12)

    def test_script_help(self):
        self.assertLines(shell('x script help'), 9, 22)


if __name__ == '__main__': 
    main()


