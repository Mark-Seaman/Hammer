from django.views.generic import ListView, DetailView

from tasks.models import Task


#-----------------------------------------------------------------------------
# List view

# Basic list view with using a template

class TaskList(ListView):
    model = Task
    template_name = 'task.html'


#-----------------------------------------------------------------------------
# Detail view

# Basic detail view
class TaskDetail(DetailView):


    model = Task
    template_name = 'task_detail.html'
