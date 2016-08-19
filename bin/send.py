import mandrill
from platform import node
from os.path import join, exists
from os import remove
from shutil import copyfile

from doc import doc_text, doc_read_text
from shell import banner, file_tree_list, read_file
from log import log


EMAIL_KEY = 'xT7vaqDAdPOY6xeM5Trcow'


def channel_details(channel):
    channels = {
        'me': { 
            'from': 'Comm System',
            'to': 'mark.b.seaman@gmail.com',
            'subject': 'Note from mark',
        },
        'test': { 
            'from': 'Test System',
            'to': 'mark.b.seaman@gmail.com',
            'subject': 'Test results',
        },
        'spiritual': { 
            'from': 'Spiritual Things',
            'to': 'mark.b.seaman@gmail.com',
            'subject': 'Meditations for Quiet Moments',
        },
        'faceblog': {
            'from': 'Faceblog Poster',
            'to': 'ether644gappy@m.facebook.com',
            'subject': 'Facebook Post',
        },
    }
    return channels.get(channel)


def send_command(args):
    if args:
        cmd = args[0]
        if cmd=='dispatch':
            send_dispatch()
        elif cmd=='doc':
            send_doc(args[1], args[2])
        elif cmd=='doc-text':
            send_doc_text(args[1], args[2])
        elif cmd=='list':
            send_list() 
        elif cmd=='show':
            show_message('me')
        else:
            send_help()
    else:
        send_help()


def send_doc(path, channel):
    #copyfile(join('Documents', path), message_path('me'))
    text = doc_text(path)
    queue_message(channel, text) 


def send_doc_text(path, channel):
    #copyfile(join('Documents', path), message_path('me'))
    text = '<pre>' + doc_read_text([path]) + '</pre>'
    queue_message(channel, text) 


def send_dispatch():
    if exists(message_path('me')):
        if send_out_mail('me'):
            remove(message_path('me'))
    elif exists(message_path('spiritual')):
        if send_out_mail('spiritual'):
            remove(message_path('spiritual'))
    elif exists(message_path('test')):
        if send_out_mail('test'):
            remove(message_path('test'))
    elif exists(message_path('faceblog')):
        if send_out_mail('faceblog'):
            remove(message_path('faceblog'))
    else:
        print('No file to send')


def send_help():
    print('''
        usage:  x send COMMAND

        COMMAND:
            dispatch -  send the queued messages to the correct channels
            doc      -  queue a formatted document
            list     -  list messages to send
            show     -  show the content of messages to send

        ''')

def send_list():
    print('send list')
    path = message_path('')
    for f in file_tree_list(path):
        print(f)


def message_path(channel):
    return join('Documents', 'send', channel)


def queue_message(channel, text):
    try:
        path = message_path(channel)
        with open(path, 'a') as f:
            f.write("%s\n" % text)
    except:
        f.write("Bad text send\n")


def show_message(channel):
    if exists(message_path(channel)):
        print(open(message_path(channel)).read())
    else:
        print('No file to send')


def read_message(channel):
    return  open(message_path(channel)).read()


def send_out_mail(channel):
    details = channel_details(channel)
    email_from  = details.get('from')
    email_to = details.get('to')
    title = details.get('subject')
    text = read_message(channel)
    return send_mail(email_from, email_to, title, text)


def send_mail(emailFrom, emailTo, title, text):
    '''Send mail using the Shrinking World Mandrill account'''

    def create_message(emailFrom, emailTo, title, body):
        return {
            'subject': title,
            'html': body,
            'from_email': 'mark.seaman@shrinking-world.com',
            'from_name': emailFrom,
            'headers': {'Reply-To': 'mark.seaman@shrinking-world.com'},
            'to': [{"email": email} for email in emailTo],
        }

    try:
        emailTo = emailTo.split(',')
        message = create_message(emailFrom, emailTo, title, text)
        mandrill_client = mandrill.Mandrill(EMAIL_KEY)
        mandrill_client.messages.send(message=message, async=False)
        print('send successful: %s' % emailTo)
        return True
    except:
        print('Error: during send_mail: To %s' % emailTo)

