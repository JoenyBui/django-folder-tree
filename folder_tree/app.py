from django.apps import AppConfig


class FolderTreeConfig(AppConfig):
    name = 'folder_tree'

    def ready(self):
        from . import signals
