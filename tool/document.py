from genericpath import exists, isfile
from os.path import isdir, join

from bin.shell import shell
from hammer.settings import BASE_DIR
from tool.log import log


def doc_dir_exists(title):
    log('doc_dir_exists', title)
    path = doc_path(title)
    if isdir(path):
        return True


def doc_path(page):
    return join(BASE_DIR, 'Documents', page)


def doc_text(page):
    return pandoc_text(doc_path(page))


def doc_link(title):
    return title.replace('.md', '')


def doc_exists(title):
    log('doc_exists',title)
    path = doc_path(title)
    if exists(path) or exists(path+'.md'):
        return not isdir(path)


def pandoc_command():
    if exists('/usr/bin/pandoc'):
        return '/usr/bin/pandoc'
    elif exists('/usr/local/bin/pandoc'):
        return '/usr/local/bin/pandoc'


def pandoc_text(path):
    log('pandoc', path)
    cmd = pandoc_command()
    if not cmd:
        return '<h1>Pandoc is not installed</h1>'
    if exists(path):
        if isfile(path):
            return shell('%s -t html %s' % (cmd, path))
        else:
            path += '/Index.md'
        if exists(path) and isfile(path):
            return shell('%s -t html %s' % (cmd, path))
        return '<h1>File Index is missing, %s</h1>' % path
    else:
        path += '.md'
        if exists(path) and isfile(path):
            return shell('%s -t html %s' % (cmd, path))

        return '<h1>File is missing, %s</h1>' % path