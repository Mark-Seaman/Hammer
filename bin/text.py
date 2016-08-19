from re import compile, search
from sys import argv

from shell import read_file


SELECTORS = {
    'functions' : {
        'match_pattern': r'def (.*)\(.*\)', 
        'select_pattern': r'\2',
    },
    'signature' : {
        'match_pattern': r'def (.*)\(.*\)', 
        'select_pattern': r'\1',
    },
    'agents': {
        'match_pattern': r'(.{40})(.{33}) +[\w\d_\-\.]+\@([\w\d_\-\.]+)', 
        'select_pattern': r'\2\4',
    },
}


def text_command(options):
    if options:
        cmd = options[0]
        args = options[1:]
        if cmd=='match':
            text_match(args[0], args[1])
        elif cmd=='no-match':
            text_no_match(args[0], args[1])
        elif cmd=='select':
            text_select(SELECTORS[args[0]], args[1])
        elif cmd=='replace':
            text_replace(args[0], args[1], args[2])
        else:
            text_help(args)
    else:
        text_help()


def text_select(selector, doc):
    match_pattern = selector['match_pattern']
    select_pattern = selector['select_pattern']
    text = read_file(doc)
    for line in text.split('\n'):
        match = compile(r'^.*(%s).*$' % match_pattern).sub(select_pattern, line)
        if match != line:
            print(match)
            

def text_match(match_pattern, doc):
    text = read_file(doc)
    for line in text.split('\n'):
        match = search(r'^.*(%s).*$' % match_pattern, line)
        if match:
            print(match.string)
            

def text_no_match(match_pattern, doc):
    text = read_file(doc)
    for line in text.split('\n'):
        match = search(r'^.*(%s).*$' % match_pattern, line)
        if not match:
            print(line)
            

def text_replace(match_pattern, replace_pattern, doc):
    text = read_file(doc)
    text = compile(match_pattern).sub(replace_pattern, text)
    print(text)


def text_help(args=None):
    print('''
        text Command

        usage: x text COMMAND

        COMMAND:

            match - show lines that match
            no_match - show lines that don't match
            replace - replace lines
            select - pattern matching in doc

        ''')


if __name__ == '__main__':

    if argv[2:]:
        text_select(SELECTORS[argv[1]], argv[2])
    elif argv[1:]:
        # Select functions from a file
        text_select(SELECTORS['functions'], argv[1])
    else:
        print('usage: x text pattern doc')
    