#!/usr/bin/env python
# Execute a python script as a command

from os import system
from sys import argv

from app import app_command
from client import client_command
from cmd import cmd_command
from collab import collab_command
from data import data_command
from faceblog import faceblog_command
from hourly import hourly_command
from tool import tool_command
from log import log_command
from doc import doc_command
from seamanslog import seamanslog_command
from send import send_command
from spiritual import spiritual_command
from src import src_command
from staging import staging_command
from text import text_command
from todo import todo_command
from web import web_command


def execute_command(cmd,args):
    if cmd=='app':
        app_command(args)
    elif cmd=='cmd':
        cmd_command(args)
    elif cmd=='client':
        client_command(args)
    elif cmd=='collab':
        collab_command(args)
    elif cmd=='data':
        data_command(args)
    elif cmd=='doc':
        doc_command(args)
    elif cmd=='faceblog':
        faceblog_command(args)
    elif cmd=='hourly':
        hourly_command(args)
    elif cmd=='log':
        log_command(args)
    elif cmd=='page':
        command_scriptor(cmd, args)
    elif cmd=='project':
        command_scriptor(cmd, args)
    elif cmd=='seamanslog':
        seamanslog_command(args)
    elif cmd=='send':
        send_command(args)
    elif cmd=='spiritual':
        spiritual_command(args)
    elif cmd=='src':
        src_command(args)
    elif cmd=='staging':
        staging_command(args)
    elif cmd=='task':
        command_scriptor(cmd, args)
    elif cmd=='text':
        text_command(args)
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

            app     # Work with application code
            cmd     # Manage command scripts
            collab  # Application collaborator
            data    # Database scripting
            doc     # Manage project documents
            hourly  # Hourly command for maintence
            log     # Manage logs
            page    # Page Master app
            project # Projects for clients
            spiritual # Spiritual Things subscriber list
            src     # Manage source code
            staging # Manage server at Digital Ocean
            task    # Task Master
            todo    # To do list command
            tool    # Manage django tool scripts
            tst     # Run tests with expected results
            web     # Web pages

        Example: x staging ip
                 x doc list
                 x tst run
        ''' % (cmd,args))


def command_scriptor(cmd, args):
    system('python manage.py scriptor %s %s' % (cmd, ' '.join(args)))


if argv[1:]:
    execute_command(argv[1], argv[2:])

else:
    command_help('',[])

