=====
Folder Tree
=====

Folder tree is a Django app to organize a folder tree hierarchy.  It is used to help the
user organize their files.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "folder_tree" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'folder_tree',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^folder_tree/', include('folder_tree.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a folder_tree (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/folder_tree/ to participate in the poll.