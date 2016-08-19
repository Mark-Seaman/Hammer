from os import environ, system

from shell import  shell
from log import log


DROPLET_IP = environ['DROPLET_IP']
SERVER_DIR = environ['SERVER_DIR']


def staging_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    log('server command %s' % options)
    if options[0:]:
        cmd = options[0]
        args = options[1:]
        if cmd=='command':
            staging_remote_command(args)
        elif cmd=='console':
            staging_console()
        elif cmd=='control':
            staging_control()
        elif cmd=='copy':
            staging_copy()
        elif cmd=='deploy':
            staging_deploy()
        elif cmd=='ip':
            staging_ip()
        elif cmd=='redeploy':
            staging_redeploy(args)
        elif cmd=='restart':
            staging_restart()
        elif cmd=='restore':
            staging_restore()
        elif cmd=='root':
            staging_root_console()
        elif cmd=='save':
            staging_save()
        elif cmd=='web':
            staging_web()
        else:
            staging_help()
    else:
        staging_help()


def staging_redeploy(args):
    print('staging_redeploy')
    print(shell(' '.join(['vc']+args)))
    staging_deploy()


def staging_help():
    print('''
        usage: x server command

        command:
            command  # Execute a command on the remote server
            console  # Log in to the remote server
            control  # Bring up the remote control panel
            copy     # Copy the django code to the server
            deploy   # Deploy code to the remote server
            help     # Show the doc commands
            ip       # Show the IP address of the server
            redeploy # Push code and deploy
            restart  # Restart the remote server
            restore  # Bring back the old files to the server
            root     # Log in as root
            save     # Save the files from the remote server
            web      # Show the web page from the remote server

        ''')

#----------------------------------------------------------------
# Commands

def staging_console():
    print('Remote console')
    system('ssh django@%s' % DROPLET_IP)


def staging_control():
    url = 'https://cloud.digitalocean.com/login'
    system('open -a "Google Chrome" '+url)


def staging_copy():
    rsync = 'rsync -auv %s/ django@%s:%s'
    #rsync = 'rsync -auv --delete %s/ django@%s:/home/django/hammer'
    cmd = rsync % (environ['p'], DROPLET_IP, SERVER_DIR)
    print('copy to remote (%s)' % cmd)
    print(shell(cmd))


def staging_deploy():
    print('remote pull')
    staging_remote_command(['git pull; cd Documents; git pull'])
    staging_restart()


def staging_ip():
    print(DROPLET_IP)


def staging_remote_command(args):
    cmd = ' '.join(args)
    bashrc = 'source %s/bin/bashrc-django>/dev/null' % SERVER_DIR
    script = "%s && %s" % (bashrc, cmd)
    ssh = 'ssh django@%s -C \"%s\"' % (DROPLET_IP, script)
    print('Remote Execution (%s)' % ssh)
    system (ssh)


def staging_restart():
    print('Remote service restart')
    system('ssh root@%s -C service gunicorn restart' % DROPLET_IP)
    #system('ssh root@%s -C service nginx restart' % DROPLET_IP)


def staging_restore():
    rsync = 'rsync -auv  %s/hammer_server/ django@%s:/home/django'
    cmd = rsync % (environ['HOME'], DROPLET_IP, )
    print('copy from remote (%s)' % cmd)
    print(shell(cmd))


def staging_root_console():
    print('Remote console')
    system('ssh root@%s' % DROPLET_IP)


def staging_save():
    rsync = 'rsync -auv  django@%s:/home/django/ %s/hammer_server'
    cmd = rsync % (DROPLET_IP, environ['HOME'], )
    print('copy from remote (%s)' % cmd)
    print(shell(cmd))


def staging_web():
    print('Remote web page')
    cmd = 'x web http://'+DROPLET_IP
    system(cmd)


