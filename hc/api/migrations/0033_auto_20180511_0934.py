# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-11 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20180511_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='membership_access',
            field=models.BooleanField(default=False),
        ),
    ]
