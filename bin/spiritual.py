from os import environ, system
from os.path import join

from doc import doc_pick, doc_path
from log import log
from shell import file_tree_list


def spiritual_command(args):
    if args:
        cmd = args[0]

        if cmd=='send':
            if args[1:]:
                spiritual_send(args[1])
            else:
                doc = doc_pick(['spiritual'])
                spiritual_send(doc)

        elif cmd=='pick':
            doc = doc_pick(['spiritual'])
            print(open(doc_path(doc)).read())
            print('     -- '+doc)

        elif cmd=='list':
            print('Spiritual List')
            for f in spiritual_list():
                print(f)

        elif cmd=='stats':
            print('Spiritual Stats')

        else:
            spiritual_help()
    else:
        spiritual_help()


def spiritual_list(dir=None):
    log('list_documents', dir)
    if dir:
        d = join(environ['p'], 'Documents', 'spiritual', dir)
    else:
        d = join(environ['p'], 'Documents', 'spiritual')
    files = file_tree_list(d)
    files = [ f.replace(d+'/','') for f in files]
    return files



def spiritual_help():
    print('''
        usage:  x spiritual spiritual_command

        command:
            list         # List the available documents
            pick         # Select an item at random
            send [doc]   # Send a doc to subscribers  
            stats        # Show stats for files      
        ''')


def spiritual_send(doc):
    system('x send doc %s spiritual' % doc)
    system('x send dispatch')


