# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_executable', models.BooleanField(default=False)),
                ('is_locked', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('file_type', models.IntegerField(choices=[(0, 'txt'), (1, 'png'), (2, 'jpg'), (3, 'jpeg'), (4, 'gif'), (5, 'bmp'), (6, 'mpg'), (7, 'mpeg'), (8, 'mov'), (9, 'avi'), (10, 'wmv'), (11, 'csv'), (12, 'pdf'), (13, 'xls'), (14, 'xlsx'), (15, 'doc'), (16, 'docx'), (17, 'ppt'), (18, 'pptx'), (-1, 'unknown')], default=-1)),
                ('file', models.FileField(upload_to='general', default='default.txt')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_executable', models.BooleanField(default=False)),
                ('is_locked', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('file_type', models.IntegerField(choices=[(1, 'png'), (2, 'jpg'), (3, 'jpeg'), (4, 'gif'), (5, 'bmp')], default=-1)),
                ('photo', models.ImageField(upload_to='photo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreeFolder',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_locked', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreeProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFolder',
            fields=[
                ('treefolder_ptr', models.OneToOneField(to='folder_tree.TreeFolder', auto_created=True, primary_key=True, parent_link=True, serialize=False)),
                ('app_type', models.IntegerField(choices=[(0, 'Wham')], default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('folder_tree.treefolder',),
        ),
        migrations.AddField(
            model_name='treeprofile',
            name='root_folder',
            field=models.ForeignKey(to='folder_tree.TreeFolder', blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='treeprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='treefolder',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', to='folder_tree.TreeFolder', blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='treefolder',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='folder',
            field=models.ForeignKey(blank=True, to='folder_tree.ProjectFolder', null=True),
        ),
        migrations.AddField(
            model_name='generalfile',
            name='folder',
            field=models.ForeignKey(blank=True, to='folder_tree.ProjectFolder', null=True),
        ),
    ]
