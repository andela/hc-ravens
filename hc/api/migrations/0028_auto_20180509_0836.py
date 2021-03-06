# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-09 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180503_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='nag_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='check',
            name='status',
            field=models.CharField(choices=[('up', 'Up'), ('down', 'Down'), ('new', 'New'), ('paused', 'Paused')], default='new', max_length=6),
        ),
    ]
