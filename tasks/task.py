from tool.log import log
from tasks.models import Task


def task_command(self,args):
    log('task %s' % args)
    if args:
        cmd = args[0]
        args = args[1:]
        if cmd=='add':
            task_add(self,args)
        elif cmd=='delete':
            task_delete(self,args)
        elif cmd=='edit':
            task_edit(self,args)
        elif cmd=='get':
            task_get(self,args)
        elif cmd=='list':
            task_list(self,args)
        else:
            task_help(self)


def task_help(self):
    self.stdout.write('''

        usage: x command 
        
        command:
            add    # add a new record
            delete # delete a task
            edit   # update a record
            get    # lookup a specific task
            help   # show command help
            list   # show a list of tasks
    ''')


def task_list(self,args):
    for t in Task.objects.all():
        self.stdout.write("ID:    %s" % t.pk)
        self.stdout.write("Name:  %s" % t.name)
        self.stdout.write("Date:  %s" % t.date)
        self.stdout.write("")


def task_add(self,args):
    if not args:
        self.stdout.write('A task must have a name')
    else:
        task = Task.objects.create()
        task_set_name(args, task)


def task_delete(self,args):
    if not args:
        #Task.objects.all().delete()
        self.stdout.write('You must specify a task')
        return

    tasks = Task.objects.filter(pk=args[0])
    if args and tasks:
        tasks[0].delete()
    else:
        self.stdout.write('Could not find task, %s' % args[0])


def task_edit(self,args):
    tasks = Task.objects.filter(pk=args[0])
    if tasks:
        task_set_name(args[1:], tasks[0])
    else:
        self.stdout.write('Could not find task, %s' % args[0])


def task_set_name(args, task):
    task.name = ' '.join(args)
    task.save()


def task_get(self,args):
    tasks = Task.objects.filter(pk=args[0])
    if tasks:
        t = tasks[0]
        self.stdout.write("ID:    %s" % t.pk)
        self.stdout.write("Name:  %s" % t.name)
        self.stdout.write("Date:  %s" % t.date)
    else:
        self.stdout.write('Could not find task, %s' % args[0])
