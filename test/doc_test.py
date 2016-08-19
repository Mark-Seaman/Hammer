from bin.shell import shell, shell_lines
from bin.switches import TEST_DOC_ENCODING


def doc_test():
    return shell_lines('x doc list', 400,450)


def doc_help_test():
    return shell_lines('x doc', 14, 20)


def doc_html_test():
    return shell_lines('x doc html ToDo', 30,31)


def doc_read_test():
    return shell_lines('x doc read ToDo',55,55)


def doc_summary_test():
    return shell('x doc summary')


def doc_encoding_test():
    if TEST_DOC_ENCODING:
        return shell('x doc test all')
    else:
        return 'doc_encoding_test is DISABLED'

