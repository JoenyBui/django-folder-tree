
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
    list_display = ['name', 'public_id', 'file_type', 'photo', 'user', 'created', 'modified']


class GeneralFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'public_id', 'file_type', 'file', 'user', 'created', 'modified']

# Register your models here.
admin.site.register(TreeProfile, TreeProfileAdmin)
admin.site.register(TreeFolder, TreeFolderAdmin)
admin.site.register(ImageFile, ImageFileAdmin)
admin.site.register(GeneralFile, GeneralFileAdmin)
admin.site.register(ProjectFolder, ProjectFolderAdmin)
