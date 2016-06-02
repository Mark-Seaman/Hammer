# Hammer URL Configuration

from django.conf.urls import url, include
from django.contrib import admin

from tool.views import doc
import tasks.urls
# import webapp.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task/', include(tasks.urls)),
    # url(r'^app/', include(webapp.urls)),
    url(r'^(?P<title>[\w/\-_.]*)',    doc),
]
