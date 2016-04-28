from os import environ, listdir, system
from os.path import join

from bin.shell import  file_path, file_list, line_count, read_file, shell_command


DROPLET_IP = '159.203.152.201'


def server_command(self, options):
    '''
    Execute a command script from scriptor.  Parse off command and args and dispatch it.
    '''
    #self.stdout.write('server command output %s' % options)
    server = options[0]
    args = options[1:]
    if server=='command':
        server_remote_command(self, args)
    elif server=='console':
        server_console(self)
    elif server=='control':
        server_control(self)
    elif server=='copy':
        server_copy(self)
    elif server=='deploy':
        server_deploy(self)
    elif server=='ip':
        server_ip(self)
    elif server=='restart':
        server_restart(self)
    elif server=='restore':
        server_restore(self)
    elif server=='root':
        server_root_console(self)
    elif server=='save':
        server_save(self)
    elif server=='web':
        server_web(self)
    else:
        server_help(self)
    

def server_help(self):
    self.stdout.write('''
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


def server_console(self):
    self.stdout.write('Remote console')
    system('ssh django@%s' % DROPLET_IP)


def server_control(self):
    url = 'https://cloud.digitalocean.com/login'
    system('open -a "Google Chrome" '+url)


def server_copy(self):
    rsync = 'rsync -auv --delete %s/simple/ django@%s:/home/django/django_project'
    cmd = rsync % (environ['p'], DROPLET_IP)
    self.stdout.write('copy to remote (%s)' % cmd)
    self.stdout.write(shell_command(cmd))


def server_deploy(self):
    self.stdout.write('remote pull')
    server_remote_command(self,['git pull'])


def server_ip(self):
    self.stdout.write(DROPLET_IP)


def server_remote_command(self, args):
    cmd = ' '.join(args)
    bashrc = 'source ~/hammer/bin/bashrc-server>/dev/null'
    script = "%s && %s" % (bashrc, cmd)
    ssh = 'ssh django@%s -C \"%s\"' % (DROPLET_IP, script)
    self.stdout.write('Remote Execution (%s)' % ssh)
    system (ssh)


def server_restart(self):
    self.stdout.write('Remote service restart')
    system('ssh root@%s -C service gunicorn restart' % DROPLET_IP)


def server_root_console(self):
    self.stdout.write('Remote console')
    system('ssh root@%s' % DROPLET_IP)


def server_save(self):
    rsync = 'rsync -auv  django@%s:/home/django/ %s/hammer_server'
    cmd = rsync % (DROPLET_IP, environ['HOME'], )
    self.stdout.write('copy from remote (%s)' % cmd)
    self.stdout.write(shell_command(cmd))


def server_restore(self):
    rsync = 'rsync -auv  %s/hammer_server/ django@%s:/home/django'
    cmd = rsync % (environ['HOME'], DROPLET_IP, )
    self.stdout.write('copy from remote (%s)' % cmd)
    self.stdout.write(shell_command(cmd))


def server_web(self):
    self.stdout.write('Remote web page')
    cmd = 'open -a "Google Chrome" http://'+DROPLET_IP
    system(cmd)

