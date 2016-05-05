from django.conf.urls import url

from tasks.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete


urlpatterns = [

    # List view
    url(r'^$', TaskList.as_view(), name='task_list'),

    # Detail view
    url(r'^(?P<pk>\d+)$', TaskDetail.as_view(), name='task-detail'),

    # Add view
    url(r'add$', TaskCreate.as_view(), name='task_add'),

    # Update view
    url(r'(?P<pk>\d+)/edit$', TaskUpdate.as_view(), name='task_update'),

    # Delete view
    url(r'(?P<pk>\d+)/delete$', TaskDelete.as_view(), name='task_delete'),
]
