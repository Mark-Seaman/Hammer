from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from webapp.models import WebApp


from django.shortcuts import render
from django.http import HttpResponse
from os.path import join, exists, dirname
from os import listdir
from subprocess import Popen,PIPE

from hammer.settings import BASE_DIR
from tool.views import format_doc

def doc(request, title):
    directory = join(BASE_DIR, 'doc')
    if exists(directory):
        path = join(directory,'app',title)
        docs = listdir(dirname(path))
        #text = 'Directory exists : %s' % ', '.join(listdir(directory))
        text = format_doc(path)
    else:
        docs = None
        text = 'Directory missing'
    data = { 'title': title, 'text': text, 'docs': docs }
    return render(request, 'webapp_doc.html', data )



# List view:  Basic list view with using a template
class WebAppList(ListView):
    model = WebApp
    template_name = 'webapp.html'

    def get_context_data(self, **kwargs):
        context = super(WebAppList, self).get_context_data(**kwargs)
        context['title'] = "Web Apps"
        return context


# Detail view:  Basic detail view
class WebAppDetail(DetailView):
    model = WebApp
    template_name = 'webapp_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(WebAppDetail, self).get_context_data(**kwargs)
        context['title'] = "Web App Detail"
        context['docs'] = [ 'Project', 'Hosting', 'App', 'Data', 'Doc', 'Script', 'Test' ]
        return context


# Create view
class WebAppCreate(CreateView):
    model = WebApp
    fields = ['name', 'notes']
    template_name = 'webapp_edit.html'
    success_url = reverse_lazy('webapp_list')

    def get_context_data(self, **kwargs):
        context = super(WebAppCreate, self).get_context_data(**kwargs)
        context['title'] = "Add New Web App"
        return context


# Update view
class WebAppUpdate(UpdateView):
    model = WebApp
    fields = ['name', 'notes']
    template_name = 'webapp_edit.html'
    success_url = reverse_lazy('webapp_list')

    def get_context_data(self, **kwargs):
        context = super(WebAppUpdate, self).get_context_data(**kwargs)
        context['title'] = "Edit Web App Info"
        return context

# Delete view
class WebAppDelete(DeleteView):
    model = WebApp
    success_url = reverse_lazy('webapp_list')
    template_name = 'webapp_delete.html'

    def get_context_data(self, **kwargs):
        context = super(WebAppDelete, self).get_context_data(**kwargs)
        context['title'] = "Delete Web App"
        return context


