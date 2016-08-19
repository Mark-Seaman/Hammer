from django.conf.urls import url, include

from tool.views import spiritual_doc
from tool.views import tool_doc, tool_home, tool_test, tool_theme


urlpatterns = [

    # Documents
    url(r'^$',                                  tool_home),

    # Test Master
    url(r'^test$',                              tool_test),

    # Theme Master
    url(r'^theme$',                             tool_theme),

    # Hammer Document Viewer
    url(r'^(?P<title>[\w/\-_.]+)',              tool_doc),
]
