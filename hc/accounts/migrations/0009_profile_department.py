# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180510_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
