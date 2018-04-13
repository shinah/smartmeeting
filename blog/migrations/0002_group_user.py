# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-13 07:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(default=None, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
