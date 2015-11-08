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
import os
import sys
import json

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters

from . import toolkit as utk

from .models import TreeProfile, TreeFolder, GeneralFile, ImageFile, ProjectFolder
from .serializers import GeneralFileSerializer, ImageFileSerializer, FolderSerializer, ProjectSerializer

__author__ = 'jbui'


class TreeFullView(APIView):
    """
    Return the tree full view.
    """

    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, format=None):
        """
        Get the JSON structure of the folder view.
        :param request:
        :return:
        """
        user = request.user
        profile = TreeProfile.objects.get(user=user)

        show_files = request.REQUEST

        # return Response(json.loads(profile.get_folder_json(show_files)))
        return Response(profile.get_children())


class JsTreeView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        profile = TreeProfile.objects.get(user=user)

        return Response(profile.get_jstree())


class FolderViewSet(viewsets.ModelViewSet):
    queryset = TreeFolder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('public_id', 'name')
    paginate_by = 100

    def get_queryset(self):
        user = self.request.user

        return TreeFolder.objects.filter(user=user)


class ProjectFolderViewSet(viewsets.ModelViewSet):
    queryset = ProjectFolder.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('public_id', 'name')
    paginate_by = 100

    def get_queryset(self):
        user = self.request.user

        return ProjectFolder.objects.filter(user=user)


class GeneralFileViewSet(viewsets.ModelViewSet):
    """
    General File View Set
    """
    queryset = GeneralFile.objects.all()
    serializer_class = GeneralFileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    filter_fields = ('name', 'file_type')

    def get_queryset(self):
        user = self.request.user

        return GeneralFile.objects.filter(user=user)


class ImageFileViewSet(viewsets.ModelViewSet):
    """
    Image file view set.
    """
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    filter_fields = ('name', 'file_type', 'photo')

    def get_queryset(self):
        user = self.request.user

        return ImageFile.objects.filter(user=user)
