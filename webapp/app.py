from tool.log import log
from webapp.models import WebApp

def webapp_command(self,args):
    log('app %s' % args)
    if args:
        cmd = args[0]
        args = args[1:]
        if cmd=='add':
            webapp_add(self,args)
        elif cmd=='delete':
            webapp_delete(self,args)
        elif cmd=='edit':
            webapp_edit(self,args)
        elif cmd=='get':
            webapp_get(self,args)
        elif cmd=='list':
            webapp_list(self,args)
        else:
            webapp_help(self)


def webapp_help(self):
    self.stdout.write('''

        usage: x command 
        
        command:
            add    # add a new record
            delete # delete a webapp
            edit   # update a record
            get    # lookup a specific webapp
            help   # show command help
            list   # show a list of webapps
    ''')


def webapp_add(self,args):
    if not args:
        self.stdout.write('A webapp must have a name')
    else:
        webapps = WebApp.objects.filter(name=name(args))
        if webapps:
            return webapps[0]
        else:
            webapp = WebApp.objects.create(name=name(args), notes='No notes')
            return webapp


def webapp_delete(self,args):
    if not args:
        #WebApp.objects.all().delete()
        self.stdout.write('You must specify a webapp')
        return
    webapps = WebApp.objects.filter(pk=args[0])
    if args and webapps:
        webapps[0].delete()
    else:
        self.stdout.write('Could not find webapp, %s' % args[0])


def webapp_edit(self,args):
    webapps = WebApp.objects.filter(pk=args[0])
    if webapps:
        webapps[0].name = name(args[1:])
        webapps[0].save()
    else:
        self.stdout.write('Could not find webapp, %s' % args[0])


def webapp_list(self,args):
    self.stdout.write("ID   Name                 Notes ")
    for t in WebApp.objects.all():
        row = "%-4s %-20s %-20s" % (t.pk, t.name, t.notes)
        self.stdout.write(row)
    self.stdout.write('')


def webapp_get(self,args):
    webapps = WebApp.objects.filter(pk=args[0])
    if webapps:
        t = webapps[0]
        self.stdout.write("ID:     %s" % t.pk)
        self.stdout.write("Name:   %s" % t.name)
        self.stdout.write("Notes:  %s" % t.notes)
        self.stdout.write('')
    else:
        self.stdout.write('Could not find webapp, %s' % args[0])


def name(args):
    return ' '.join(args)


