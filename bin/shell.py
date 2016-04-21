from os import environ, system, walk
from os.path import join
from platform import node
from selenium import webdriver
from subprocess import Popen,PIPE
from unittest import TestCase, main


def shell_command(cmd):
    '''Execute a shell command and return stdout'''
    return Popen(cmd.split(), stdout=PIPE).stdout.read()


def read_file(path):
    '''Read a file and return the text'''
    return open(path).read()


def file_list(path):
    '''Return a list of files in the directory tree'''
    files = []
    for root, dirnames, filenames in walk(path):
        if not '.git' in root: 
            for filename in filenames:
                files.append(filename)
    return files


def hostname():
    return node()
