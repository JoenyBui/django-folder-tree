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

from django.test import TestCase
from django.contrib.auth.models import User

from .models import TreeProfile
from .models import TreeFolder
from .models import TreeFile

from .toolkit import initializing_user_session

__author__ = 'jbui'


class TreeFolderProfileTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username="test1",
                                           email="test1@email.com",
                                           password="password")
        self.u2 = User.objects.create_user(username='test2',
                                           email="test2@email.com",
                                           password='password')

        initializing_user_session(self.u1)
        self.u1.save()

        self.f1 = self.u1.treeprofile.create_tree_folder(name='f1', parent=self.u1.treeprofile.root_folder)
        self.f2a = self.u1.treeprofile.create_tree_folder(name='f2a', parent=self.f1)
        self.f2b = self.u1.treeprofile.create_tree_folder(name='f2b', parent=self.f1)
        self.f3 = self.u1.treeprofile.create_tree_folder(name='f3', parent=self.f2a)

    def test_initialize_user_session(self):
        self.assertIsNotNone(self.u1.treeprofile)

    def test_root_folder(self):
        self.assertEqual(self.u1.treeprofile.root_folder.name, 'root')

    def test_create_folder(self):
        self.assertTrue(self.u1.treeprofile.get_children())
        self.assertEqual(len(TreeFolder.objects.all()), 5)

    def test_delete_folder(self):
        tree_initial = self.u1.treeprofile.get_children()
        self.u1.treeprofile.delete_folder(self.f2a)
        tree_after = self.u1.treeprofile.get_children()

        self.assertNotEqual(tree_initial, tree_after)
        self.assertEqual(len(TreeFolder.objects.all()), 5)

