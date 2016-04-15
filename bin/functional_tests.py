from os import environ, system, walk
from os.path import join
from platform import node
from selenium import webdriver
from subprocess import Popen,PIPE
from unittest import TestCase, main

#from functional_tests.tests import  FunctionalTestCase

RUN_WEB_BROWSER = True


def shell_command(cmd):
    return Popen(cmd.split(), stdout=PIPE).stdout.read()


def file_list(path):
    files = []
    for root, dirnames, filenames in walk(path):
        if not '.git' in root: 
            for filename in filenames:
                files.append(filename)
    return files


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)


class PythonTest(TestCase):

    def test_python_version(self):
        import sys
        expected = "sys.version_info(major=2, minor=7, micro=10, releaselevel='final', serial=0)"
        self.assertEqual(str(sys.version_info), expected)

    def test_virtual_env(self):
        cmd = ['which', 'python']
        output = Popen(cmd, stdout=PIPE).stdout.read()
        expected = '/Users/seaman/Tools/env-python27/bin/python\n'
        self.assertEqual(output,expected)

    def test_pip_list(self):
        path = join(environ['p'],'bin','pip-list')
        expected = open(path).read()
        self.assertEqual(shell_command('pip list'), expected)


class FilesTest(TestCase):

    def test_file_count(self):
        files = file_list(environ['p'])
        self.assertLess(len(files), 40)


class SystemTest(TestCase):

    def test_system_hostname(self):
        host = node()
        self.assertIn ('iMac', host)


class DjangoTest(TestCase):

    def test_django_directory(self):
        files = file_list(join(environ['p'],'hammer'))
        #print(files)
        self.assertEqual(len(files), 9)

    def test_tool_directory(self):
        files = file_list(join(environ['p'],'tool'))
        #print(files)
        self.assertEqual(len(files), 11)



if __name__ == '__main__': 
    main()


