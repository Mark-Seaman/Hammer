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
        self.assertEqual(shell_command('git status'), '')


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
        expected = '''apt-xapian-index (0.45)\nargparse (1.2.1)\nchardet (2.0.1)\nCheetah (2.4.4)\ncloud-init (0.7.5)\ncolorama (0.2.5)\nconfigobj (4.7.2)\nDjango (1.6.1)\ndjango-extensions (1.6.1)\ngevent (1.0)\ngreenlet (0.4.2)\ngunicorn (17.5)\nhtml5lib (0.999)\njsonpatch (1.3)\njsonpointer (1.0)\nLandscape-Client (14.12)\noauth (1.0.1)\nPAM (0.4.2)\npip (1.5.4)\nprettytable (0.7.2)\npsycopg2 (2.4.5)\npyOpenSSL (0.13)\npyserial (2.6)\npython-apt (0.9.3.5ubuntu1)\npython-debian (0.1.21-nmu2ubuntu2)\nPyYAML (3.10)\nrequests (2.2.1)\nsetuptools (3.3)\nsix (1.5.2)\nSouth (0.7.5)\nssh-import-id (3.21)\nTwisted-Core (13.2.0)\nurllib3 (1.7.1)\nvirtualenv (1.11.4)\nwheel (0.24.0)\nwsgiref (0.1.2)\nzope.interface (4.0.5)\n'''
        output = shell_command('pip list')
        self.assertEqual(output, expected)


if __name__ == '__main__': 
    main()
