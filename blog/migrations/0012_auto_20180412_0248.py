# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180411_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_belong',
            name='g1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Group'),
        ),
    ]