# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-03 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_group_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]