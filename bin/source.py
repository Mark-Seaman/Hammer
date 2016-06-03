from log import log


def source_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    log('Cmd command output %s' % options)
    if not options:
        source_help()
    else:
        cmd = options[0]
        args = options[1:]
        if cmd=='list':
            source_list(args)
        else:
            source_help()


def source_help():
    print('''
        usage: x source command

        command:
            diff     # Calculate difference from other source
            edit     # Edit a specific document file
            help     # Show the commands
            list     # List the available commands
            length   # Measure the lines in each doc
            read     # Show the text from all document

        ''')


def source_list(args):
    print('source list', args)
