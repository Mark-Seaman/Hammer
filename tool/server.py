from os import environ, listdir, system
from os.path import join

from bin.shell import  file_path, file_list, line_count, read_file, shell_command


DROPLET_IP = '45.55.115.15'


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
            help     # Show the doc commands

        ''')


def server_remote_command(self, args):
    cmd = ' '.join(args)
    cmd = 'ssh root@%s -C %s' % (DROPLET_IP,cmd)
    self.stdout.write('Remote Execution (%s)' % cmd)
    self.stdout.write(shell_command(cmd))


def server_control(self):
    url = 'https://cloud.digitalocean.com/login'
    system('open -a "Google Chrome" '+url)


def server_deploy(self):
    def copy_to_remote(directory):
        cmd = 'rsync -auv %s/%s/ root@%s:/home/django/django_project/%s'
        cmd = cmd % (environ['p'], directory, DROPLET_IP, directory)
        self.stdout.write('copy to remote (%s)' % cmd)
        self.stdout.write(shell_command(cmd))
    copy_to_remote('bin')
    


def server_console(self):
    self.stdout.write('Remote console')
    system('ssh root@%s' % DROPLET_IP)