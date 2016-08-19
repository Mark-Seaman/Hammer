
from os import environ
from os.path import join

from bin.shell import file_tree_list, shell, shell_lines


def text_help_test():
    return shell('x text')

def text_functions_test():
    return shell_lines('x text select functions tool/views.py', 12, 12)

def text_match_test():
    return shell_lines('x text match def tool/views.py', 12, 12)

def text_no_match_test():
    return shell_lines('x text no-match def tool/views.py', 90, 90)


    