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

from . import views

__author__ = 'jbui'

# The API URLS are now determined automatically by the router.
# Additionally, we include the login URLS for the browsable API.
urlpatterns = [
    url(r'^new/$', views.FolderNewView.as_view(), name='new'),
    url(r'^delete/$', views.FolderNewView.as_view(), name='delete'),
    url(r'^$', views.FolderView.as_view(), name='index'),
]
