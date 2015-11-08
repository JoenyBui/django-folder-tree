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

from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import RequestContext, loader

__author__ = 'jbui'


class FolderView(View):
    """
    Render folder view.
    """
    # @method_decorator(login_required)
    # @method_decorator(csrf_protect)
    def get(self, request):
        user = self.request.user
        return render(request, 'folder_tree/index.html', {'username': str(user),})


class FolderNewView(View):
    """
    Render new folder.
    """
    # @method_decorator(login_required)
    # @method_decorator(csrf_protect)
    def get(self, request):
        user = self.request.user
        return render(request, 'folder_tree/new.html', {'username': str(user),})


class FolderDeleteView(View):
    """
    Render delete folder.
    """
    # @method_decorator(login_required)
    # @method_decorator(csrf_protect)
    def get(self, request):
        user = self.request.user
        return render(request, 'folder_tree/delete.html', {'username': str(user),})
