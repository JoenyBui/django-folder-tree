
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


class FolderSerializer(serializers.ModelSerializer):
    """
    Folder serializer

    """

    class Meta:
        model = TreeFolder
        fields = ('id', 'name', 'parent', 'is_locked', 'created', 'modified')


class ProjectSerializer(serializers.ModelSerializer):
    """
    Folder serializer

    """

    class Meta:
        model = ProjectFolder
        fields = ('id', 'name', 'app_type', 'parent', 'is_locked', 'created', 'modified')


class GeneralFileSerializer(serializers.ModelSerializer):
    """
    A general file type for results file.  This should not account for input file.

    """

    class Meta:
        model = GeneralFile
        fields = ('id', 'name', 'folder', 'file_type', 'file', 'is_executable', 'is_locked', 'created', 'modified')


class ImageFileSerializer(serializers.ModelSerializer):
    """
    Image file serializer.

    """

    class Meta:
        model = ImageFile
        fields = ('id', 'name', 'folder', 'file_type', 'photo', 'is_executable', 'is_locked', 'created', 'modified')
