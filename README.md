# README

Folder Tree
------

Folder tree is a Django app to organize a folder tree hierarchy.  It is used to help the
user organize their files.

Detailed documentation is in the "docs" directory.

Branch
------
1. master
    main branch where the source code of HEAD always reflect a production-ready state

2. develop
    main branch where the source code of HEAD always reflects a state where the latest development changes for the next release

3. feature branches
    used to develop new features for the upcoming or a distant future release

    a. May branch off from:
        develop
    b. Must merge back into:
        develop
    c. Branch naming convention:
        anything except master, develop, release-*, or hotfix-*

4. Release branches
    support preparation of a new production release

    a. May branch off from:
        develop
    b. Must merge back into:
        develop and master
    c. Branch naming convention:
        release-*

5. Hotfix
    much like release branches in that they are also meant to prepare for a new production

    a. May branch off from:
        master
    b. Must merge back into:
        develop and master
    c. Branching naming convention:
        hotfix-*


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
