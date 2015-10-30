# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('folder_tree', '0003_treeprofile_public_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='treefolder',
            name='public_id',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
    ]
