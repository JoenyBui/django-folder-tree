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
import uuid
from collections import OrderedDict

from django.utils.six import BytesIO
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers

from .models import TreeFolder, GeneralFile, ImageFile, ProjectFolder

from . import global_setting as gs

__author__ = 'jbui'


class FolderSerializer(serializers.Serializer):
    """
    Folder serializer
    """
    public_id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    name = serializers.CharField(max_length=255)
    parent_id = serializers.UUIDField()

    def to_representation(self, instance):
        ret = super(FolderSerializer, self).to_representation(instance)

        if instance.parent:
            ret["parent_id"] = instance.parent.public_id
        else:
            ret["parent_id"] = None

        return ret

    def create(self, validated_data):
        """

        """
        parent_id = validated_data.get('parent_id')
        name = validated_data.get('name')
        public_id = validated_data.get('public_id')

        try:
            parent = TreeFolder.objects.filter(public_id=parent_id).first()
        except ObjectDoesNotExist as e:
            parent = None

        if parent:
            user = self.context['request'].user

            return TreeFolder.objects.create(name=name, public_id=public_id, user=user, parent=parent)
        else:
            return None


class ProjectSerializer(serializers.Serializer):
    """
    Folder serializer
    """
    public_id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    name = serializers.CharField(max_length=255)
    parent_id = serializers.UUIDField()
    app_type = serializers.IntegerField()

    def to_representation(self, instance):
        ret = super(ProjectSerializer, self).to_representation(instance)

        if instance.parent:
            ret["parent_id"] = instance.parent.public_id
        else:
            ret["parent_id"] = None

        return ret

    def create(self, validated_data):
        """

        """
        parent_id = validated_data.get('parent_id')
        name = validated_data.get('name')
        public_id = validated_data.get('public_id')
        app_type = validated_data.get('app_type')

        try:
            parent = ProjectFolder.objects.filter(public_id=parent_id).first()
        except ObjectDoesNotExist as e:
            parent = None

        if parent:
            user = self.context['request'].user

            return TreeFolder.objects.create(name=name, public_id=public_id, user=user, parent=parent)
        else:
            return None


class GeneralFileSerializer(serializers.Serializer):
    """
    A general file type for results file.  This should not account for input file.
    """
    public_id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    name = serializers.CharField(max_length=255)
    file_type = serializers.IntegerField()
    file = serializers.FileField()
    folder_id = serializers.UUIDField()

    def to_representation(self, instance):
        ret = super(GeneralFileSerializer, self).to_representation(instance)

        if instance.folder:
            ret["folder_id"] = instance.folder.public_id
        else:
            ret["folder_id"] = None

        return ret

    def create(self, validated_data):
        """
        Create a new file entry.

        User must provide a valid folder UUID.
        """
        folder_id = validated_data.get('folder_id')
        name = validated_data.get('name')
        file_type = validated_data.get('file_type')
        file = validated_data.get('file')
        public_id = validated_data.get('public_id')

        try:
            folder = ProjectFolder.objects.filter(public_id=folder_id).first()
        except ObjectDoesNotExist as e:
            folder = None

        if folder:
            user = self.context['request'].user

            return GeneralFile.objects.create(name=name, public_id=public_id, user=user, folder=folder,
                                              file_type=file_type, file=file)
        else:
            return None


class ImageFileSerializer(serializers.Serializer):
    """
    Image file serializer.
    """
    public_id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    name = serializers.CharField(max_length=255)
    photo = serializers.ImageField()
    file_type = serializers.IntegerField()
    folder_id = serializers.UUIDField()

    def to_representation(self, instance):
        ret = super(ImageFileSerializer, self).to_representation(instance)

        if instance.folder:
            ret["folder_id"] = instance.folder.public_id
        else:
            ret["folder_id"] = None

        return ret

    def create(self, validated_data):
        """
        Create a new file entry.

        User must provide a valid folder UUID.
        """
        folder_id = validated_data.get('folder_id')
        name = validated_data.get('name')
        file_type = validated_data.get('file_type')
        photo = validated_data.get('photo')
        public_id = validated_data.get('public_id')

        try:
            folder = ProjectFolder.objects.filter(public_id=folder_id).first()
        except ObjectDoesNotExist as e:
            folder = None

        if folder:
            user = self.context['request'].user

            return GeneralFile.objects.create(name=name, public_id=public_id, user=user, folder=folder,
                                              file_type=file_type, photo=photo)
        else:
            return None
