from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from webapp.models import WebApp


# List view:  Basic list view with using a template
class WebAppList(ListView):
    model = WebApp
    template_name = 'webapp.html'

    def get_context_data(self, **kwargs):
        context = super(WebAppList, self).get_context_data(**kwargs)
        context['title'] = "Edit Web App Info"
        return context


# Detail view:  Basic detail view
class WebAppDetail(DetailView):
    model = WebApp
    template_name = 'webapp_detail.html'


# Create view
class WebAppCreate(CreateView):
    model = WebApp
    fields = ['name', 'notes']
    template_name = 'webapp_edit.html'
    success_url = reverse_lazy('webapp_list')


# Update view
class WebAppUpdate(UpdateView):
    model = WebApp
    fields = ['name', 'notes']
    template_name = 'webapp_edit.html'
    success_url = reverse_lazy('webapp_list')


# Delete view
class WebAppDelete(DeleteView):
    model = WebApp
    success_url = reverse_lazy('webapp_list')
    template_name = 'webapp_delete.html'
