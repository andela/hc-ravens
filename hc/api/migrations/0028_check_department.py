# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180503_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]