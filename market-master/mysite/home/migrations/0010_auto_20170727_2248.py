# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170727_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
