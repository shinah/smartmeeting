# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-13 03:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20180413_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]