from unittest import TestCase, main

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)


class PythonTest(TestCase):

    def test_python_version(self):
        import sys
        expected = "sys.version_info(major=2, minor=7, micro=10, releaselevel='final', serial=0)"
        self.assertEqual(str(sys.version_info), expected)

    def test_virtual_env(self):
        from subprocess import Popen,PIPE
        cmd = ['which', 'python']
        output = Popen(cmd, stdout=PIPE).stdout.read()
        expected = '/Users/seaman/Tools/env-python27/bin/python\n'
        self.assertEqual(output,expected)


if __name__ == '__main__': 
    main()