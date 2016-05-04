from django.views.generic import ListView

# from django.shortcuts import render

from tasks.models import Task


#-----------------------------------------------------------------------------
# List view

# Basic list view with using a template

class TaskList(ListView):
    model = Task
    template_name = 'task.html'
