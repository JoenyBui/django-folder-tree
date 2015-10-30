# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('folder_tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('previous_folder', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='generalfile',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='generalfile',
            name='modified',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='modified',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='treefolder',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='treefolder',
            name='modified',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trash',
            name='folder',
            field=models.ForeignKey(to='folder_tree.TreeFolder'),
        ),
        migrations.AddField(
            model_name='trash',
            name='profile',
            field=models.ForeignKey(to='folder_tree.TreeProfile'),
        ),
    ]
