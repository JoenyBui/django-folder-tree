
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
