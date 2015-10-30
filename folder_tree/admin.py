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

from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import TreeProfile, TreeFolder, GeneralFile, ProjectFolder, ImageFile


class TreeProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'public_id', 'user', 'root_folder']


class TreeFolderAdmin(MPTTModelAdmin):
    mptt_level_index = 20
    list_display = ['name', 'public_id', 'user', 'created', 'modified']


class ProjectFolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'public_id', 'user', 'app_type']


class ImageFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'file_type', 'photo', 'user', 'created', 'modified']


class GeneralFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'file_type', 'file', 'user', 'created', 'modified']

# Register your models here.
admin.site.register(TreeProfile, TreeProfileAdmin)
admin.site.register(TreeFolder, TreeFolderAdmin)
admin.site.register(ImageFile, ImageFileAdmin)
admin.site.register(GeneralFile, GeneralFileAdmin)
admin.site.register(ProjectFolder, ProjectFolderAdmin)
