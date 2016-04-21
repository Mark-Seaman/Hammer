from os import environ, system, walk
from os.path import join
from platform import node
from selenium import webdriver
from subprocess import Popen,PIPE
from unittest import TestCase, main


def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    return Popen(cmd.split(), stdout=PIPE).stdout.read()

def read_file(path):
    '''Read a file and return the text'''
    return open(path).read()

def file_list(path):
    '''Return a list of files in the directory tree'''
    files = []
    for root, dirnames, filenames in walk(path):
        if not '.git' in root: 
            for filename in filenames:
                files.append(filename)
    return files



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
        self.assertBetween(len(file_list(path)), min, max)


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
        self.assertLength(output, expected)


class FilesTest(FunctionalTestCase):

    def test_file_count(self):
        files = file_list(environ['p'])
        self.assertBetween(len(files), 48,55)


class SystemTest(FunctionalTestCase):

    def test_system_hostname(self):
        host = node()
        self.assertTrue ('iMac' in host or 'macbook' in host)


class DjangoTest(FunctionalTestCase):

    def test_django_directory(self):
        self.assertFiles(join(environ['p'],'hammer'), 8,10)

    def test_tool_directory(self):
        self.assertFiles(join(environ['p'],'tool'), 18,21)

    def test_django_version(self):
        self.assertIn('Django (1.9.4)', shell_command('pip list'))


class DocTest(FunctionalTestCase):

    def test_documents(self):
        self.assertLines(shell_command('x doc list'), 4,5)

    def test_doc_length(self):
        self.assertLines(shell_command('x doc length'), 4,5)

    def test_doc_read(self):
        self.assertLines(shell_command('x doc read'), 270,300)


class AutomationTest(FunctionalTestCase):

    def test_automation(self):
        self.assertLines(shell_command('x test'), 4,10)

    def test_log(self):
        self.assertLines(shell_command('x log'), 13,20)

    def test_log_clear(self):
        self.assertEqual(shell_command('x log clear'), 'Logs cleared\n')

    def test_help(self):
        self.assertLines(shell_command('x help'), 12,12)


if __name__ == '__main__': 
    main()


