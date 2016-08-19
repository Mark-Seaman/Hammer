#!/usr/bin/env python

from os import environ, system
from os.path import  join
from platform import node
from sys import argv


def web(page):
    '''Open a web page in Google Chrome'''
    url = page
    if not page.startswith('http://') and not page.startswith('https://'):
        url = 'http://' + page
    # Use the correct invocation
    if 'iMac' in node() or 'mac' in node() or 'mini' in node():
        system('open -a "Google Chrome" '+url)
    else:
        system('rbg google-chrome '+url)


def web_path(topic=None):
    path = environ['pb']
    if topic:
        path = join(path,topic)
    return path


def web_help():
    '''Show all the web webs and their usage.'''
    print('''
    usage:  web cmd [args]

    cmd:

        dev         - Local website
        github      - Go the Github site
        mandrill    - Email sending service
        mybook      - My Book Online website
        tech        - Seaman Tech website
        time        - Track time for project

            ''')

def web_command(args):
    '''Execute all of the web specific webs'''
    if args:
        cmd = args[0]
    else:
        web_help()
        cmd = 'dev'

    if cmd == 'client':
        web('http://seaman-tech.com/tech/client/%s' % ''.join(args[1:]))

    elif cmd == 'collab':
        web('http://seaman-tech.com/tech/collab/%s' % ''.join(args[1:]))

    elif cmd=='dev':
        web('http://localhost:8003/%s' % ''.join(args[1:]))

    elif cmd=='github':
        web('https://github.com/Shrinking-World/MyBook.git')

    elif cmd=='mandrill':
        web('http://mandrill.com')

    elif cmd=='mybook':
        web('http://mybookonline.org')

    elif cmd=='tech':
        web('http://seaman-tech.com')

    elif cmd=='time':
        web('http://shrinkingworld.harvestapp.com')

    else:
        web(cmd)


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    web_command(argv)

