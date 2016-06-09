# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 01:07
from __future__ import unicode_literals

import archapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('basic', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('oftype', models.IntegerField(choices=[(1, 'Integer'), (2, 'Boolean'), (3, 'Double'), (4, 'String')], default=1, verbose_name='Value type')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=archapp.models.Image.content_filename)),
                ('oftype', models.IntegerField(choices=[(1, 'General'), (2, 'Plane'), (3, 'Photo'), (4, 'Found')], default=1, verbose_name='Image type')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=False, verbose_name='Boolean value')),
                ('integer', models.IntegerField(default=0, verbose_name='Integer value')),
                ('double', models.FloatField(default=0.0, verbose_name='Float value')),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.TextField(blank=True, max_length=128, verbose_name='String value')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='archapp.Property')),
            ],
            options={
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
                'db_table': 'archapp_property_translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('data', picklefield.fields.PickledObjectField(editable=False)),
                ('props', models.ManyToManyField(to='archapp.Property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFilter',
            fields=[
                ('filter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archapp.Filter')),
                ('title', models.TextField(default='User-defined filter', max_length=128)),
                ('query', picklefield.fields.PickledObjectField(editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('archapp.filter',),
        ),
        migrations.AddField(
            model_name='property',
            name='instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archapp.Filter', verbose_name='Related filter'),
        ),
        migrations.AddField(
            model_name='image',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archapp.Site'),
        ),
        migrations.AddField(
            model_name='filter',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfilters', to='archapp.Filter'),
        ),
        migrations.AlterUniqueTogether(
            name='propertytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
