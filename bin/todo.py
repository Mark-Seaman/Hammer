#!/usr/bin/env python

from sys import argv
from os import system, environ
from os.path import join

def todo_command(options):

    # Extract the input arguments to form new todo item
    text = ' '.join(options)[:80]
    print('To Do List: ' + text)

    # Append to file
    f = join(environ['p'], 'doc', 'ToDo.md')
    open(f, 'a').write(text+'\n')

    # Show the items
    print(open(f).read())

    # Edit the items
    system('e '+f)
