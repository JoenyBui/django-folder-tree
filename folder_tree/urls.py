
from django.conf.urls import url, include

from . import views

__author__ = 'jbui'

# The API URLS are now determined automatically by the router.
# Additionally, we include the login URLS for the browsable API.
urlpatterns = [
    url(r'^new/$', views.FolderNewView.as_view(), name='new'),
    url(r'^delete/$', views.FolderNewView.as_view(), name='delete'),
    url(r'^$', views.FolderView.as_view(), name='index'),
]
