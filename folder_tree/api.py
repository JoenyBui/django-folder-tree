from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .viewsets import TreeFullView, GeneralFileViewSet, ImageFileViewSet, FolderViewSet, ProjectFolderViewSet, JsTreeView

__author__ = 'jbui'


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'file', GeneralFileViewSet, 'file')
router.register(r'image', ImageFileViewSet, 'image')
router.register(r'folder', FolderViewSet, 'folder')
router.register(r'project', ProjectFolderViewSet, 'project')

urlpatterns = [
    url(r'^', include(router.urls)),
]
