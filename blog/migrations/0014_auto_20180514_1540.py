# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-14 06:40
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20180511_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toDo', models.TextField()),
                ('deadline', models.DateField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='takes', to='blog.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
