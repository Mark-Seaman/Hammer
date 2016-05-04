from django.conf.urls import url
from django.http import HttpResponse

from tool.views import home

def home(request):
        title = "World's Simplest App"
        text = '''
        This is the simplest Django app that is possible. All extra stuff has
        been stripped out. Only essential code remains. .
        '''
        return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,text))

urlpatterns = [
    url(r'^$', home)
]
