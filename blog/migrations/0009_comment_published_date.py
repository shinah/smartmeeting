# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-10 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]