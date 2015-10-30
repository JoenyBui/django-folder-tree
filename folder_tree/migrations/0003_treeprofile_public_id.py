# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('folder_tree', '0002_auto_20151030_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='treeprofile',
            name='public_id',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
    ]
