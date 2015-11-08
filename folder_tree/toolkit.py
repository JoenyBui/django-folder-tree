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

import re

__author__ = 'jbui'


def split_path(path):
    """
    Given path split it into list array.
    :param path:
    :return:
    """
    delimiters = "/", "\\"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, path)


def initializing_user_session(user):
    """
    Initialize the user for the dashboard.
    :param user:
    """
    from .models import TreeProfile

    # Check to see if the user has a tree profile.  If not then create one and sync to server.
    if not hasattr(user, 'treeprofile'):
        profile = TreeProfile(user=user)
        profile.create_root()
        profile.save()


def tree_item_to_dict(item):
    """
    Create tree item to dictionary.
    :param item:
    :return:
    """
    if item:
        value = dict(
            public_id=item.public_id,
            name=item.name,
            children=[tree_item_to_dict(i) for i in item.get_children()]
        )

        return value
    else:
        return None

def jstree_item_to_dict(item, array):
    """
    Return a jstree of the folder structure.
    :param item:
    :param array:
    :return:
    """
    if item:
        for child_item in item.get_children():
            array.append(dict(id=child_item.public_id, parent=item.public_id, text=child_item.name, state=dict(opened=False)))

            jstree_item_to_dict(child_item, array)
    else:
        return False