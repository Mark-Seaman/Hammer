from os import environ, listdir, system
from os.path import abspath
from platform import node

from shell import  file_path, file_list, line_count, read_file, shell_command
from log import log


def web_command(options):
    log('web command output %s' % options)
    if options[0:]:
        cmd = options[0]
        args = options[1:]
        if cmd=='file':
            web_file(args[0])
        elif cmd=='firefox':
            web_firefox(args[0])
        elif cmd=='index':
            web_page('http://localhost:8000/README.md')
        elif cmd=='page':
            web_page(args[0])
        elif cmd=='todo':
            web_page('http://localhost:8000/ToDo.md')
        else:
            web_help()
    else:
        web_page('localhost:8000')


def web_help():
    print('''
        usage: x web [command]

        command:
            file [file] # Show a file in the browser
            firefox     # Run the firefox browser
            index       # Show the README page
            page [page] # Show the remote page in the browser
            todo        # Show the todo list

        ''')


#----------------------------------------------------------------
# Commands

def web_file(f):
    f = 'file://'+abspath(f)
    chrome = '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"'
    system('%s %s' % (chrome,f) )


def web_page(page):
    '''Open a web page in Google Chrome'''
    url = page
    if not page.startswith('http://') and not page.startswith('https://'):
        url = 'http://' + page
    if 'mac' in node() or 'iMac' in node() or 'us-west' in node():
        system('open -a "Google Chrome" '+url)
    else:
        system('rbg google-chrome '+url)


def web_firefox(page):
    if 'mac' in node() or 'iMac' in node() or 'us-west' in node():
        system('open -a "Firefox" '+page)
    else:
        system('rbg firefox '+page)

