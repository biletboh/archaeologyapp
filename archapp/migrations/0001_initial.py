# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 05:35
from __future__ import unicode_literals

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
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=128, upload_to='uploads/')),
                ('oftype', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=False, verbose_name='Boolean value')),
                ('integer', models.IntegerField(default=0, verbose_name='Integer value')),
                ('double', models.FloatField(default=0.0, verbose_name='Float value')),
                ('string', models.TextField(blank=True, max_length=128, verbose_name='String value')),
                ('oftype', models.IntegerField(choices=[(0, 'Integer'), (1, 'Boolean'), (2, 'Double'), (3, 'String')], default=0, verbose_name='Value type')),
                ('linked', models.BooleanField(default=False, verbose_name='Use as a subfilter')),
            ],
            options={
                'verbose_name_plural': 'properties',
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
    ]
