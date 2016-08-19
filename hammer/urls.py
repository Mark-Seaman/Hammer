# Hammer URL Configuration
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


import tool.urls


urlpatterns = [

    url(r'^robots.txt$', RedirectView.as_view(url=staticfiles_storage.url('robots.txt'), permanent=True), name="robots"),
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'), permanent=True), name="favicon"),

    url(r'^admin/',      admin.site.urls),

    url(r'^',            include(tool.urls)),

]
