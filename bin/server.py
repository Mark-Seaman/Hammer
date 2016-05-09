from os import environ, system

from shell import  shell_command
from log import log

DROPLET_IP = '159.203.152.201'


def server_command(options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    log('server command %s' % options)
    if options[0:]:
        cmd = options[0]
        args = options[1:]
        if cmd=='command':
            server_remote_command(args)
        elif cmd=='console':
            server_console()
        elif cmd=='control':
            server_control()
        elif cmd=='copy':
            server_copy()
        elif cmd=='deploy':
            server_deploy()
        elif cmd=='ip':
            server_ip()
        elif cmd=='restart':
            server_restart()
        elif cmd=='restore':
            server_restore()
        elif cmd=='root':
            server_root_console()
        elif cmd=='save':
            server_save()
        elif cmd=='web':
            server_web()
        else:
            server_help()
    else:
        server_help()


def server_help():
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
            restart  # Restart the remote server
            restore  # Bring back the old files to the server
            root     # Log in as root
            save     # Save the files from the remote server
            web      # Show the web page from the remote server

        ''')

#----------------------------------------------------------------
# Commands

def server_console():
    print('Remote console')
    system('ssh django@%s' % DROPLET_IP)


def server_control():
    url = 'https://cloud.digitalocean.com/login'
    system('open -a "Google Chrome" '+url)


def server_copy():
    rsync = 'rsync -auv %s/django_project/ django@%s:/home/django/django_project'
    #rsync = 'rsync -auv --delete %s/ django@%s:/home/django/hammer'
    cmd = rsync % (environ['p'], DROPLET_IP)
    print('copy to remote (%s)' % cmd)
    print(shell_command(cmd))


def server_deploy():
    print('remote pull')
    server_remote_command(['git pull'])
    server_restart()


def server_ip():
    print(DROPLET_IP)


def server_remote_command(args):
    cmd = ' '.join(args)
    bashrc = 'source ~/hammer/bin/bashrc-server>/dev/null'
    script = "%s && %s" % (bashrc, cmd)
    ssh = 'ssh django@%s -C \"%s\"' % (DROPLET_IP, script)
    print('Remote Execution (%s)' % ssh)
    system (ssh)


def server_restart():
    print('Remote service restart')
    system('ssh root@%s -C service gunicorn restart' % DROPLET_IP)
    #system('ssh root@%s -C service nginx restart' % DROPLET_IP)


def server_restore():
    rsync = 'rsync -auv  %s/hammer_server/ django@%s:/home/django'
    cmd = rsync % (environ['HOME'], DROPLET_IP, )
    print('copy from remote (%s)' % cmd)
    print(shell_command(cmd))


def server_root_console():
    print('Remote console')
    system('ssh root@%s' % DROPLET_IP)


def server_save():
    rsync = 'rsync -auv  django@%s:/home/django/ %s/hammer_server'
    cmd = rsync % (DROPLET_IP, environ['HOME'], )
    print('copy from remote (%s)' % cmd)
    print(shell_command(cmd))


def server_web():
    print('Remote web page')
    cmd = 'x web page http://'+DROPLET_IP
    system(cmd)


