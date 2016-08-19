from django.conf.urls import url, include

from tool.views import spiritual_doc
from tool.views import tool_doc, tool_home, tool_task, tool_test, tool_theme, tool_seamanslog
from tool.project import ProjectList, ProjectDetail, ProjectCreate, ProjectUpdate, ProjectDelete


#import collab.urls
#import contact.urls
from hire.views import hire_home
# import spiritual.urls
import tasks.urls
import thot.urls


urlpatterns = [

    # Documents
    url(r'^$',                                  tool_home),

    # # Client
    # url(r'^client$',                            client_doc),
    # url(r'^client/(?P<title>[\w\/\-_.]+)',      client_doc),

    # Project Views
    url(r'^project/$',                          ProjectList.as_view(),     name='project_list'),
    url(r'^project/(?P<pk>\d+)$',               ProjectDetail.as_view(),   name='project-detail'),
    url(r'^project/add$',                       ProjectCreate.as_view(),   name='project_add'),
    url(r'^project/(?P<pk>\d+)/edit$',          ProjectUpdate.as_view(),   name='project_update'),
    url(r'^project/(?P<pk>\d+)/delete$',        ProjectDelete.as_view(),   name='project_delete'),

    # Seaman's Log
    url(r'^seamanslog$', tool_seamanslog),

    # Spiritual Things
    url(r'^spiritual$', spiritual_doc),
    url(r'^spiritual/(?P<title>[\w\/\-_.]+)$',  spiritual_doc),

    # Task Master
    url(r'^task$',                              tool_task),
    url(r'^task/(?P<id>\d+)$',                  tool_task),

    # Test Master
    url(r'^test$',                              tool_test),

    # Theme Master
    url(r'^theme$',                             tool_theme),

    # New URLS
    #url(r'^collab', include(collab.urls)),
    # url(r'^contact/',    include(contact.urls)),
    url(r'^hire$', hire_home),
    url(r'^hire/(?P<page>[\w/\-_.]*)$', hire_home),
    # url(r'^spiritual',   include(spiritual.urls)),
    url(r'^task/', include(tasks.urls)),
    url(r'^thot/', include(thot.urls)),

    # Hammer Document Viewer
    url(r'^(?P<title>[\w/\-_.]+)',              tool_doc),
]
