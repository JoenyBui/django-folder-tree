from django.conf.urls import url, include

from rest_framework import routers

# from rest_framework.routers import DefaultRouter

from .viewsets import TreeFullView, GeneralFileViewSet, ImageFileViewSet, FolderViewSet, ProjectFolderViewSet, JsTreeView

# profile_root

__author__ = 'jbui'


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
# router.register(r'', TreeProfileViewSet)

# profile_router = routers.NestedSimpleRouter(router, 'profile', lookup='profile')
# router = DefaultRouter()

# router.register(r'folder', TreeFolderViewSet)
router.register(r'file', GeneralFileViewSet)
router.register(r'image', ImageFileViewSet)
router.register(r'folder', FolderViewSet)
router.register(r'project', ProjectFolderViewSet)
# The API URLS are now determined automatically by the router.
# Additionally, we include the login URLS for the browsable API.

urlpatterns = [
    # url(r'^tree', TreeFullView.as_view()),
    # url(r'^jstree', JsTreeView.as_view()),
    url(r'^', include(router.urls)),
]
