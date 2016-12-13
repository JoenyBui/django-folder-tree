
from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import TreeProfile, TreeFolder, GeneralFile, ProjectFolder, ImageFile


class TreeProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'root_folder']


class ProjectFolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'app_type', 'created', 'modified']


class ImageFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file_type', 'photo', 'user', 'created', 'modified']


class GeneralFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file_type', 'file', 'user', 'created', 'modified']


# Register your models here.
admin.site.register(TreeProfile, TreeProfileAdmin)
admin.site.register(TreeFolder,
                    DraggableMPTTAdmin)
admin.site.register(ImageFile, ImageFileAdmin)
admin.site.register(GeneralFile, GeneralFileAdmin)
admin.site.register(ProjectFolder, ProjectFolderAdmin)
