# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_finder', '0002_auto_20161016_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarysecondaryneed',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='resource_finder.Facility'),
        ),
    ]
