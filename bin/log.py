from os import environ
from os.path import join


def log_path():
    if environ.get('p'):
        return join(environ['p'], 'log', 'hammer.log')
    else:
        from hammer.settings import BASE_DIR
        return join(BASE_DIR, 'log', 'hammer.log')


def log_command(options):
    '''
    Execute a log command script from scriptor.  Parse off command and args and dispatch it.
    '''
    if options[:]:
        cmd = options[0]
        args = options[1:]
        if cmd=='clear':
            log_clear()
    else:
        log_read()


def log(label,value=None):
    if value:
        label = '%s: %s' % (label, value)
    open(log_path(), 'a').write(label+'\n')


def log_exception():
    log('**Exception** -- traceback %s' % traceback.format_exc())


def log_clear():
    open(log_path(), 'w').write('')
    print('Logs cleared')


def log_read():
    text = '\n'.join(open(log_path()).read().split('\n')[-100:])
    print(text)

