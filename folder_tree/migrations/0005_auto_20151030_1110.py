# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('folder_tree', '0004_treefolder_public_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalfile',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
