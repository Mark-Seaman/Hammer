from os import environ, system, listdir, getcwd
from os.path import join, isfile, exists, isdir
from random import choice

from shell import  file_path, file_tree_list, line_count, read_file, shell
from log import log


def doc_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    log('doc command %s' % options)
    if options:
        doc = options[0]
        args = options[1:]
        if doc=='commit':
            doc_commit(args)
        elif doc=='edit':
            doc_edit(args)
        elif doc=='html':
            doc_html(args)
        elif doc=='list':
            doc_list(args)
        elif doc=='length':
            doc_length()
        elif doc=='pick':
            print(doc_pick(args))
        elif doc=='read':
            doc_read(args)
        elif doc=='send':
            doc_send(args)
        elif doc=='status':
            doc_status()
        elif doc=='summary':
            doc_summary(args)
        elif doc=='test':
            doc_test(args[0])
        else:
            doc_help()
    else:
        doc_help()


def doc_commit(args):
    comment = ' '.join(args)
    system ('''#!/bin/bash
        # Commit all files to Git repo
        cd $p/Documents
        git add -A . &&
        git commit -m"%s" &&
        git pull &&
        git push
    ''' % comment)


def doc_edit(args):
    path = file_path('Documents', args[0])
    print(shell('e %s' % path))


def doc_help():
    print('''
        usage: x doc command

        command:
            commit      # Commit all pending changes
            edit        # Edit a specific document file
            help        # Show the doc commands
            html        # Format the HTML using pandoc
            list        # List the available documents
            length      # Measure the lines in each documents
            pick        # Select a document from the tree
            read        # Show the text from all documents
            send        # Send me a copy of this doc (markdown)
            send-text   # Send me a copy of this doc (text)
            status      # Show git status
            summary     # Show the stats for the documents
            test        # Test the doc for char encoding

        ''')


def doc_html(args):
    #print('pandoc %s' % doc_path(args[0]))
    print(pandoc_text(doc_path(args[0])))


def doc_text(page):
    path = doc_path(page)
    return pandoc_text(path)


def doc_list(args=None):
    if args:
        d = args[0]
        for f in list_documents(d):
            print(join(d,f))
    else:
        for f in list_documents():
            print(f)


def doc_length(args=None):
    if args:
        d = args[0]
    else:
        d = None
    # for f in list_documents(d):
    #     fp = doc_path(f)
    #     print('%s : %d' % (f, line_count(fp)))
   

def doc_path(doc):
    if doc:
        return file_path('Documents', doc)
    else:
        return file_path('Documents')


def doc_pick(args):
    if args:
        d = args[0]
        f = d + '/' + choice(list_documents(d))
    else:
        d = None
        f = choice(list_documents())
    return f


def doc_random_select(directory):
    '''Select content from a random file in the directory'''
    from hammer.settings import BASE_DIR
    path = join(BASE_DIR, doc_path(directory))
    log('doc_random_select -- dir', path)
    select = choice(listdir(path))
    path = join('/' + directory, select)
    log('doc_random_select',  path)
    return path


def doc_redirect(page):
    log('doc_redirect', page)
    from hammer.settings import BASE_DIR
    path = join(BASE_DIR, doc_path(page))
    #log('doc_redirect -- path', path)
    if exists(path) and isdir(path) and \
        (exists(path + '/Index') and isfile(path + '/Index')) or \
        (exists(path + '/Index.md') and isfile(path + '/Index.md')):
        if page:
            new_page = '/'+ page + '/Index'
        else:
            new_page = '/Index'
        log('doc_redirect --> %s' % new_page)
        return new_page


def doc_read(args):
    text = doc_read_text(args)
    print(text)


def doc_read_text(args):
    if args:
        path = file_path('Documents', args[0])
        return read_file (path)
    else:
        files = list_documents()
        for f in files:
            path = file_path('Documents', f)
            return read_file(path)


def doc_send(args):
    if args:
        path = doc_path('send/me')
        text = pandoc_text(doc_path(args[0]))
        open(path,'w').write(text+'\n')
        print(shell('x send dispatch'))
    else:
        print('usage: doc send doc-path')


def doc_send_text(args):
    if args:
        path = doc_path('send/me')
        text = open(doc_path(args[0])).read()
        open(path,'w').write(text+'\n')
        print(shell('x send dispatch'))
    else:
        print('usage: doc send doc-path')


def doc_summary(args):
    print('Document Summary')
    if args:
        dir = join(environ['p'], 'Documents', args[0])
        d = args[0]
    else:
        dir = join(environ['p'], 'Documents')
        d = None
    files = file_tree_list(dir)
    stats = {}
    print('\n%-48s %8s %8s\n' % ('file', 'lines', 'words'))
    lines,words = 0,0
    for doc in files:
        if d:
            doc = doc.replace(dir, d)
        else:
            doc = doc.replace(dir+'/', '')
        path = join(environ['p'], 'Documents', doc)
        text = read_file(path)
        stats[doc] = [len(text.split('\n')), len(text.split())]
        print('%-50s%8s%8s' % (doc, stats[doc][0], stats[doc][1]))
        lines += stats[doc][0]
        words += stats[doc][1]
    print('\n     Totals:  %s %-30s %8s %8s\n' % (len(files), 'files', lines, words))


def doc_status():
    system ('cd $p/Documents; git status')


def list_documents(dir=None):
    log('list_documents', dir)
    if dir:
        d = join(environ['p'], 'Documents', dir)
    else:
        d = join(environ['p'], 'Documents')
    files = file_tree_list(d)
    files = [ f.replace(d+'/','') for f in files]
    return files


def doc_test(path):
    if path=='all':
        #print('test doc: '+path)
        d = ''
        for f in list_documents(dir=d):
            doc_test(join(d,f))
    else:
        #print('test doc: '+path)
        text = doc_text(path).encode('ascii', 'ignore')
        #print(path, len(text))
        try:
            open('/tmp/doc_test','w').write(text)
        except:
            print('bad document: '+path)

def pandoc_text(path):

    def format_doc (path):
        path = doc_exists(path)
        if path:
            return shell('%s -t html %s' % (cmd, path))
        return '<h1>File Index is missing, %s</h1>' % path

    def doc_exists(path):
        if exists(path):
            if isdir(path):
                if exists(path + '/Index'):
                    path += '/Index'
                else:
                    if exists(path + '/Index.md'):
                        path += '/Index.md'
                    else:
                        path = None
        else:
            if exists(path + '.md'):
                path += '.md'
            else:
                path = None
        return path

    def pandoc_command():
        if exists('/usr/bin/pandoc'):
            return '/usr/bin/pandoc'
        elif exists('/usr/local/bin/pandoc'):
            return '/usr/local/bin/pandoc'

    log('pandoc_text', path)
    cmd = pandoc_command()
    if not cmd:
        return '<h1>Pandoc is not installed</h1>'
    return format_doc(path)
