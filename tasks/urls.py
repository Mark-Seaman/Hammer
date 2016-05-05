from django.conf.urls import url


from tasks.views import TaskList, TaskDetail

urlpatterns = [

    # List view
    url(r'^$', TaskList.as_view(), name='task_list'),

    # Detail view
    url(r'^(?P<pk>\d+)$', TaskDetail.as_view(), name='task-detail'),


]
