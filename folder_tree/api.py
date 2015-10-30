"""
 *  PROTECTION ENGINEERING CONSULTANTS CONFIDENTIAL
 *
 *  [2014] - [2015] Protection Engineering Consultants
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Protection Engineering Consultants and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Protection Engineering Consultants
 * and its suppliers and may be covered by U.S. and Foreign Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Protection Engineering Consultants.
"""

from django.conf.urls import patterns, url, include
from django.conf.urls import url, include

from rest_framework import routers

# from rest_framework.routers import DefaultRouter

from .viewsets import TreeFullView, GeneralFileViewSet, ImageFileViewSet, FolderViewSet, ProjectFolderViewSet

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
    # url(r'^$', profile_root),
    url(r'^', include(router.urls)),
    url(r'^tree', TreeFullView.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
#
# urlpatterns += router.urls
# urlpatterns += profile_router.urls
