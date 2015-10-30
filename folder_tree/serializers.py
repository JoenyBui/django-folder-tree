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

from rest_framework import serializers

from .models import TreeProfile, TreeFolder, GeneralFile, ImageFile

__author__ = 'jbui'


class TreeProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TreeProfile
        fields = ('id', 'user', 'root_folder',)


class TreeFolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = TreeFolder
        fields = ('id', 'name', 'parent', 'created', 'modified')

    def is_valid(self):
        data = super(TreeFolderSerializer, self).is_valid()

        #TODO: Need to validate if the folder exists.

        return data


class GeneralFileSerializer(serializers.ModelSerializer):
    """
    A general file type for results file.  This should not account for input file.
    """
    class Meta:
        model = GeneralFile
        fields = ('id', 'name', 'file', 'file_type', 'folder', 'created', 'modified')

    def is_valid(self):
        data = super(GeneralFileSerializer, self).is_valid()

        #TODO: Need to validate the file.

        return data


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ('id', 'name', 'photo', 'file_type', 'folder', 'created', 'modified')

    def is_valid(self):
        data = super(ImageFileSerializer, self).is_valid()

        #TODO: Need to validate the file.

        return data
