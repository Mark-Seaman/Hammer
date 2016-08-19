# Hammer URL Configuration

from django.conf.urls import url, include
from django.contrib import admin

from tool.views import doc


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<title>[\w/\-_.]*)',    doc),
]
