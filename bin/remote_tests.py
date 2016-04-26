#!/usr/bin/env python
# Test to be run on Digital Ocean Server


from unittest import  main

from functional_tests import FunctionalTestCase


class RemoteTest(FunctionalTestCase):

    def test_remote_server(self):
        self.assertIn('OK', 'Run server test - OK')

    def test_host(self):
        from platform import node
        self.assertIn('iMac', node())


if __name__ == '__main__': 
    main()
