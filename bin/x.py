#!/usr/bin/env python
# Execute a python script as a command

from os import system
from sys import argv

from cmd import cmd_command
from data import data_command
from tool import tool_command
from log import log_command
from doc import doc_command
from server import server_command
from todo import todo_command
from web import web_command


def execute_command(cmd,args):
    if cmd=='app':
        command_scriptor(cmd, args)
    elif cmd=='cmd':
        cmd_command(args)
    elif cmd=='data':
        data_command(args)
    elif cmd=='Documents':
        doc_command(args)
    elif cmd=='log':
        log_command(args)
    elif cmd=='server':
        server_command(args)
    elif cmd=='task':
        command_scriptor(cmd, args)
    elif cmd=='todo':
        todo_command(args)
    elif cmd=='tool':
        tool_command(args)
    elif cmd=='tst':
        command_scriptor(cmd, args)
    elif cmd=='web':
        web_command(args)

    else:
        command_help(cmd,args)


def command_help(cmd,args):
    print('''
        Command not found, %s %s

        usage: x cmd [args]

        cmd

            cmd    # Manage command scripts
            Documents    # Manage project documents
            log    # Manage logs
            todo   # To do list command
            tool   # Manage django tool scripts
            tst    # Run tests with expected results
            server # Manage server at Digital Ocean

        Example: x server ip
                 x Documents list
                 x tst run
        ''' % (cmd,args))


def command_scriptor(cmd, args):
    system('python manage.py scriptor %s %s' % (cmd, ' '.join(args)))


if argv[1:]:
    execute_command(argv[1], argv[2:])

else:
    command_help('',[])

