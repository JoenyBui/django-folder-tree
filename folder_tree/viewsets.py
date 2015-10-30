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

from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import toolkit as utk

from .models import TreeProfile, TreeFolder, GeneralFile, ImageFile
from .serializers import TreeProfileSerializer, TreeFolderSerializer, GeneralFileSerializer, ImageFileSerializer

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
        user = self.request.user
        profile = TreeProfile.objects.get(user=user)

        show_files = request.REQUEST

        return Response(json.loads(profile.get_folder_json(show_files)))


class TreeProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """
    queryset = TreeProfile.objects.all()
    serializer_class = TreeProfileSerializer
    permission_classes = (permissions.IsAdminUser, )


class TreeFolderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = TreeFolder.objects.all()
    serializer_class = TreeFolderSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user

        return TreeFolder.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            serializer.object.user = self.request.user

            if serializer.object.is_valid(serializer.errors, **utk.clean_json(request.data)):
                obj = serializer.save(force_insert=True)

                # Create folder in the directory.
                obj.create_folder()

                self.post_save(obj, created=True)
                obj.save()

                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneralFileViewSet(viewsets.ReadOnlyModelViewSet):
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


class ImageFileViewSet(viewsets.ReadOnlyModelViewSet):
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
