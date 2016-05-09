from django.conf.urls import url

from webapp.views import WebAppList, WebAppDetail, WebAppCreate, WebAppUpdate, WebAppDelete


urlpatterns = [

    # List view
    url(r'^$', WebAppList.as_view(), name='webapp_list'),

    # Detail view
    url(r'^(?P<pk>\d+)$', WebAppDetail.as_view(), name='webapp-detail'),

    # Add view
    url(r'add$', WebAppCreate.as_view(), name='webapp_add'),

    # Update view
    url(r'(?P<pk>\d+)/edit$', WebAppUpdate.as_view(), name='webapp_update'),

    # Delete view
    url(r'(?P<pk>\d+)/delete$', WebAppDelete.as_view(), name='webapp_delete'),
]
