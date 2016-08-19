from os import system

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from log import log
from models import Project
from tool.models import Project


def project_add(self, args):
    if not args:
        self.stdout.write('no project requested')
    else:
        try:
            name = ' '.join(args)
            Project.objects.create(name=name)
            self.stdout.write('added project %s' % name)
        except:
            self.stdout.write('project is already present %s' % name)


def project_command(self, options):
    log('project command %s' % options)

    if not options:
        project_help(self)
    else:
        cmd = options[0]
        args = options[1:]
        if cmd == 'add':
            project_add(self, args)
        elif cmd == 'delete':
            project_delete(self, args)
        elif cmd == 'list':
            project_list(self)
        elif cmd == 'edit':
            project_edit(self, args)
        elif cmd == 'get':
            project_get(self, args)
        else:
            project_help(self)


def project_delete(self, args):
    if args:
        if args[0] == 'all':
            self.stdout.write('delete all projects')
            Project.objects.all().delete()
        else:
            name = ' '.join(args)
            self.stdout.write('delete projects %s' % name)
            Project.objects.get(name=name).delete()
    else:
        self.stdout.write('no project given')


def project_get(self, args):
    if args:
        name = ' '.join(args)
        p = Project.objects.get(name=name)
        if p:
            self.stdout.write('%s' % p.name)
    else:
        self.stdout.write('no project given')


def project_help(self):
    self.stdout.write('''

        script to manage projects on servers

        usage: x project command

        command

        List:
            list                - list the configured project
            get   name          - get a project by name lookup

        Modify:
            add     name user   - add a new project record
            delete  name        - remove this project
            edit    name value  - rename the project

        I/O 
            import              - import all records from a file 
            export              - export all records to a file 

        ''')


def project_list(self):
    self.stdout.write('project list')
    for p in Project.objects.all().order_by('pk'):
        print('%s.  %s  %s' % (p.pk, p.name, p.user))


def project_lookup(name):
    if Project.objects.filter(name=name):
        return Project.objects.get(name=name)


# --------------------------------
# Project Views


# List view
class ProjectList(ListView):
        model = Project
        template_name = 'project_list.html'


# Detail view
class ProjectDetail(DetailView):
        model = Project
        template_name = 'project_detail.html'


# Add view
class ProjectCreate(CreateView):
        model = Project
        fields = ['name','user']
        template_name = 'project_edit.html'


# Edit view
class ProjectUpdate(UpdateView):
        model = Project
        fields = ['name', 'user']
        template_name = 'project_edit.html'


# Delete view
class ProjectDelete(DeleteView):
        model = Project
        success_url = reverse_lazy('project_list')
        template_name = 'project_confirm_delete.html'