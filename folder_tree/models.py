import os
import shutil
import json
import logging

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey
from mptt.utils import tree_item_iterator

from . import toolkit as utk
from . import global_setting as gs

__author__ = 'jbui'

log = logging.getLogger(__name__)


def user_file_path(instance, filename):
    """
    User File Path

    :param instance:
    :param filename:
    :return:
    """
    d = timezone.now()

    return '{0}/{1}/{2}/{3}/{4}'.format(
        instance.user.id,
        d.year,
        d.month,
        d.day,
        filename)


class TreeFolder(MPTTModel):
    """
    Tree folder is used to link a file tree structure that is used to replicate what will be stored in
    the servers.  The user will create a new folder (or remove) and then progress afterwards.

    :type name: folder name
    :type parent: parent key
    :type user: user model
    :type is_locked: If folder/files locked from changes.
    :type created: created date
    :type modified: modified date

    """
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_locked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    modified = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    def __str__(self):
        """

        :return:
        """
        return 'Folder: %s' % self.name

    def save(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        self.modified = timezone.now()

        super(TreeFolder, self).save(*args, **kwargs)

    class MPTTMeta:
        """
        That MPTTMeta class adds some tweaks to django-mptt - in this case, just order_insertion_by.
        This indicates the natural ordering of the data in the tree.
        """
        order_insertion_by = ['name']

    def get_file_type(self):
        """
        Return the folder file type.

        :return:
        """
        if hasattr(self, 'projectfolder'):
            return self.projectfolder.get_file_type()
        else:
            return 'folder'

    def is_valid(self, error, **kwargs):
        """
        Is valid for the user.

        :param error:
        :param kwargs:
        :return:
        """
        valid = True

        # Need to make sure that the parent folder key is the same user as the current folder key.
        if self.parent:
            if self.parent.user != self.user:
                valid = False
                error['user'] = 'Folder does not belong to user.'

        if kwargs.get('path'):
            parent = TreeProfile.get_tree_folder(self.user, kwargs.get('path'))
            if not parent:
                valid = False
                error['path'] = '%s is not valid' % kwargs.get('path')
            else:
                self.parent = parent

        name = kwargs.get('name')

        if parent and name:
            # Path already exists.
            for folder in parent.get_children():
                if folder.name == name:
                    error['name'] = 'Path already exists: %s%s%s' % (parent.virtual_folder, os.pathsep, name)
                    valid = False

        return valid

    def get_path(self):
        """
        Get the path of the folder including the home folder.

        :return:
        """
        path = self.name

        new_folder = self.parent
        while new_folder:
            path = os.path.join(new_folder.name, path)
            new_folder = new_folder.parent

        return path

    @property
    def virtual_folder(self):
        """
        Return the virtual folder of the path.

        :return:
        """
        folders = [self.name]

        new_folder = self.parent
        while new_folder:
            folders.append(new_folder.name)
            new_folder = new_folder.parent

        path = ""
        for name in folders[:-1]:
            path = os.path.join(name, path)

        return path

    def create_folder(self):
        """
        Create the folder of the path.

        """
        path = os.path.join(gs.LOCATION_USER_STORAGE, self.get_path())

        if not os.path.isdir(path):
            os.mkdir(path)

    def delete_folder(self):
        """
        Get the path with the delete folder.

        """
        path = os.path.join(gs.LOCATION_USER_STORAGE, self.get_path())

        if os.path.isdir(path):
            shutil.rmtree(path)

        self.delete()


class TreeProfile(models.Model):
    """
    Tree Profile is used to link with django user.  This gives the user the ability to create a MPTT file structure
    in the database quickly.

    The User Profile model inherits from Django's Model class and linked to the base User class through a one-to-one
    relationship.

    :type user: user model
    :type root_folder: folder root

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    root_folder = models.ForeignKey(TreeFolder, null=True, blank=True, default=True)

    def __str__(self):
        return self.user.username

    def get_children(self):
        """
        Get children

        :return:
        """
        root = self.root_folder

        return utk.tree_item_to_dict(root)

    def get_jstree(self):
        """

        :return:
        """
        # { id : 'ajson1', parent : '#', text : 'Simple root node', state: { opened: true} },
        # { id : 'ajson2', parent : '#', text : 'Root node 2', state: { opened: true} },
        # { id : 'ajson3', parent : 'ajson2', text : 'Child 1', state: { opened: true} },
        # { id : 'ajson4', parent : 'ajson2', text : 'Child 2' , state: { opened: true}}
        root = self.root_folder

        jstree = [dict(
            id=root.id,
            parent='#',
            text=root.name,
            state=dict(opened=True)
        )]

        utk.jstree_item_to_dict(root, jstree)

        return jstree


    @staticmethod
    def get_tree_folder(user, path):
        """
        Get the tree folder given the path.

        :param user:
        :param path:
        :return:
        """
        folder = None

        uprof = TreeProfile.objects.get(user=user)
        root_folder = uprof.root_folder

        if root_folder:
            folder = root_folder

            paths = utk.split_path(path)

            for folder_name in paths[:]:
                if folder_name == '' or folder_name == user.username:
                    continue
                else:
                    for cur_folder in folder.get_children():
                        if cur_folder.name == folder_name:
                            folder = cur_folder

                            # Found the folder, so we leave the folder.
                            break

                    # If we can't find the folder, then we exit loop.
                    if not folder:
                        return None

        return folder

    @property
    def root_path(self):
        """
        Root path.

        :return:
        """
        return self.root_folder.name

    @property
    def root_virtual_path(self):
        """
        Root virtual path.

        :return:
        """
        return os.path.join(self.root_folder.name)

    def create_root(self):
        """
        Create a root node in the database, and the folder in the storage disk.

        """
        self.root_folder = TreeFolder.objects.create(user=self.user, name='root', parent=None)

    def delete_root(self):
        """
        Delete the root folder with everything underneath.

        """
        pass

    def create_tree_folder(self, name, parent):
        """
        Create tree folder.

        :param name: Name of folder
        :param parent: Parent tree folder.
        :return:
        """
        folder = TreeFolder.objects.create(name=name, user=self.user, parent=parent)
        folder.save()

        return folder

    def create_folder(self, path, force_path=True):
        """
        Given a path, create a TreeFolder.

        :param path: path of the folder to create.
        :param force_path: if the intermediary folder does not exists, create it
        """
        texts = utk.split_path(path)

        new_folder = self.root_folder
        folder_path = self.root_path

        for folder in texts[1:]:
            # Look inside the storage to see if the system has the folder.
            folder_found = False

            # Get the folders item.
            for folder_item in new_folder.get_children():
                if folder_item.name == folder:
                    new_folder = folder_item

                    if utk.is_dir(folder_path, folder):
                        folder_path = os.path.join(folder_path, folder)
                        folder_found = True
                    else:
                        if force_path:
                            folder_path = utk.make_dir(folder_path, folder)
                            folder_found = True
                        else:
                            return False
                    # Exit loop
                    break

            # If there is no children folder - force the folder create.
            if not folder_found:
                if force_path:
                    # Create a new folder.
                    new_folder = TreeFolder.objects.create(name=folder, parent=new_folder, is_locked=False)
                    folder_path = utk.make_dir(folder_path, folder)
                else:
                    return False

        return True

    def delete_folder(self, folder):
        """
        Delete a folder given a path.

        :param folder: path of the folder to delete.
        """
        if isinstance(folder, TreeFolder):
            trash = Trash.objects.create(profile=self, folder=folder, previous_folder=folder.parent.id)
            trash.save()

            folder.parent = None
            folder.save()
        else:
            #TODO: Check if it's a primary key
            #TODO: Otherwise check if it's a path.
            pass

        return True

    def get_folder(self, path):
        """
        Return the tree folder given the path.

        :param path:
        :return:
        """
        folder_names = utk.split_path(path)

        folder = self.root_folder

        for name in folder_names[1:]:
            for folder_child in folder.get_children():
                if folder_child.name == name:
                    folder = folder_child
                    pass

        return folder

    def get_path(self, path):
        """
        Pass a path and then we parse it to the real path.

        :param path:
        :return:
        """
        texts = utk.split_path(path)
        texts[0] = self.root_folder.name

        return os.sep.join(texts)

    def get_folder_json(self, show_files):
        """
        Get the json folder structure.

        :param show_files:
        :return:
        """
        data = {
            'data': utk.tree_item_to_dict(self.root_folder, show_files)
        }

        # Change the first root node label to the current user name.
        data['data']['text'] = self.user.username

        return json.dumps(data)


class ProjectFolder(TreeFolder):
    """
    Project folder.

    :type app_type: application type

    """
    app_type = models.IntegerField(choices=gs.JOB_TYPE, default=1)

    def get_file_type(self):
        """
        Return the folder file type.

        :return:
        """
        return 'project_folder'

    def get_path(self):
        """
        Get the path of the folder including the home folder.

        :return:
        """
        path = self.name

        new_folder = self.parent
        while new_folder:
            path = os.path.join(new_folder.name, path)
            new_folder = new_folder.parent

        return path


class TreeFile(models.Model):
    """
    Parent tree file for application type file.
    File will only exists within project folders, ensuring that there is no subdirectory outside
    of the the project folder app.

    :type name:
    :type user:
    :type folder: project folder model
    :type is_executable: check if the files is executable.
    :type is_locked: folder/files locked from changes.
    :type created:
    :type modified:
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User)
    folder = models.ForeignKey(ProjectFolder, null=True, blank=True)
    is_executable = models.BooleanField(default=False, blank=True)
    is_locked = models.BooleanField(default=False)
    created = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    modified = models.DateTimeField(null=False, blank=True, auto_now_add=True)

    def __str__(self):
        return 'File: %s' % self.name

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # Update modified date.
        self.modified = timezone.now()

        super(TreeFile, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                   update_fields=update_fields)

    def is_valid(self, error, **kwargs):
        return True

    @property
    def real_path(self):
        """
        Find the real path of the code.

        :return:
        """
        return os.path.join(gs.LOCATION_USER_STORAGE, self.folder.get_path(), self.get_file_name())

    @property
    def virtual_path(self):
        """
        Virtual path.

        :return:
        """
        return os.path.join(self.folder.get_path(), self.get_file_name())

    def create_file(self):
        """
        Create a new file.

        """
        root_folder = self.folder

    def get_file_name(self):
        """
        Base class needs to override this method.

        OVERRIDE THIS METHOD
        :return:
        """
        return self.name

    def delete_file(self):
        pass


class Trash(models.Model):
    """
    Trash folder.

    :type profile: one-to-many relationship
    :type prev: original parent folder
    """
    profile = models.ForeignKey(TreeProfile, on_delete=models.CASCADE)
    prev = models.ForeignKey(TreeFolder, null=True, blank=True)


class InputFile(TreeFile):
    """
    Input File.

    :type name:
    :type user:
    :type folder: project folder model - one input file equals to one project folder
    :type is_executable: check if the files is executable.
    :type is_locked: folder/files locked from changes.
    :type created:
    :type modified:
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User)
    folder = models.OneToOneField(ProjectFolder, on_delete=models.CASCADE)
    is_executable = models.BooleanField(default=False, blank=True)
    is_locked = models.BooleanField(default=False)
    created = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    modified = models.DateTimeField(null=False, blank=True, auto_now_add=True)

    def header(self):
        return "#!^%s^!#"

    def folder_name(self):
        return "%s_%d_%s" % (self.header(), self.id, self.name)

    class Meta:
        abstract = True

    @property
    def real_folder(self):
        """
        Read folder.

        :return:
        """
        return os.path.join(gs.LOCATION_USER_STORAGE, self.folder.get_path())

    @property
    def virtual_folder(self):
        """
        Virtual folder

        :return:
        """
        return os.path.join(self.folder.get_path())

    @property
    def real_path(self):
        """
        Find the real path of the code.

        :return:
        """
        return os.path.join(self.real_folder, self.get_file_name())

    # @property
    # def virtual_path(self):
    #     """
    #     Virtual path of the input path.
    #     :return:
    #     """
    #     return os.path.join(self.virtual_folder, self.get_file_name())

    def create_input_folder(self):
        """
        Create input folder.
        """
        path = self.real_folder

        if not os.path.isdir(path):
            os.mkdir(path)


class ImageFile(TreeFile):
    """
    Create an image file.

    :type file_type:
    :type photo:
    """
    file_type = models.IntegerField(choices=gs.IMAGE_TYPE, default=-1)
    photo = models.ImageField(upload_to=user_file_path)


class GeneralFile(TreeFile):
    """
    Create results field for the files that exist in the storage bin.

    :type file_type:
    :type file:

    """
    file_type = models.IntegerField(choices=gs.FILE_TYPE, default=-1)
    file = models.FileField(upload_to=user_file_path, default='default.txt')

    def set_ext(self, ext_name):
        """
        determine the extensions from the last name.

        :param ext_name:
        """
        for id, name in gs.FILE_TYPE:
            if name == ext_name.lower()[1:]:
                self.file_type = id
                break

    def get_file_name(self):
        """
        Return the filename with extension.

        :return:
        """
        return self.name + '.' + gs.FILE_TYPE[self.file_type][1]

    def get_file_type(self):
        """
        Return file type.

        :return:
        """
        return gs.FILE_TYPE[self.file_type][1]

    def get_mime(self):
        """
        Return the mime type for the file.

        :return:
        """
        return gs.get_mime(self.file_type)

    def send_message(self, email):
        """
        Send message of the file.

        :param email: email address
        :return:
        """
        subject = 'Subject here'
        message = 'Here is the message'

        try:
            attachment = self.folder

            mail = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            mail.send()

        except SystemError:
            log.error('Send Message.')
