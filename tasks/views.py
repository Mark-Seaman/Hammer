from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from tasks.models import Task


# List view:  Basic list view with using a template
class TaskList(ListView):
    model = Task
    template_name = 'task.html'


# Detail view:  Basic detail view
class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'


# Create view
class TaskCreate(CreateView):
    model = Task
    fields = ['name', 'date', 'notes','hours','done']
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task_list')


# Update view
class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'date', 'notes','hours','done']
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task_list')


# Delete view
class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_delete.html'
