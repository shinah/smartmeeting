# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-08 04:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180507_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='post',
        ),
    ]