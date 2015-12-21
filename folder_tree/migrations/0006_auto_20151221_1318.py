# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_tree', '0005_auto_20151030_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfolder',
            name='app_type',
            field=models.IntegerField(default=1, choices=[(1, 'WhAM')]),
        ),
    ]
