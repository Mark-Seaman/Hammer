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
    elif server=='deploy':
        server_deploy(self)
    elif server=='ip':
        server_ip(self)
    elif server=='restart':
        server_restart(self)
    elif server=='root':
        server_root_console(self)
    else:
        server_help(self)
    

def server_help(self):
    self.stdout.write('''
        usage: x server command

        command:
            command  # Execute a command on the remote server
            console  # Log in to the remote server
            control  # Bring up the remote control panel
            deploy   # Deploy code to the remote server
            ip       # Show the IP address of the server
            restart  # Restart the remote server
            root     # Log in as root
            help     # Show the doc commands

        ''')


def server_ip(self):
    self.stdout.write(DROPLET_IP)


def server_remote_command(self, args):
    cmd = ' '.join(args)
    bashrc = 'source ~/hammer/bin/bashrc-server>/dev/null'
    cmd = 'ssh django@%s "%s && %s"' % (DROPLET_IP, bashrc, cmd)
    self.stdout.write('Remote Execution (%s)' % cmd)
    system(cmd)


def server_control(self):
    url = 'https://cloud.digitalocean.com/login'
    system('open -a "Google Chrome" '+url)


def server_deploy(self):
    def copy_to_remote():
        cmd = 'rsync -auv %s/ django@%s:/home/django/hammer'
        cmd = cmd % (environ['p'], DROPLET_IP)
        self.stdout.write('copy to remote (%s)' % cmd)
        self.stdout.write(shell_command(cmd))
    def remote_pull():
        self.stdout.write('remote pull')
        server_remote_command(self,['git pull'])
    #copy_to_remote()
    remote_pull()

def server_console(self):
    self.stdout.write('Remote console')
    system('ssh django@%s' % DROPLET_IP)


def server_root_console(self):
    self.stdout.write('Remote console')
    system('ssh root@%s' % DROPLET_IP)

def server_restart(self):
    self.stdout.write('Remote service restart')
    system('ssh root@%s -C service gunicorn restart' % DROPLET_IP)
