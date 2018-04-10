# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Group(models.Model):
  group_name = models.CharField(max_length=100)
  group_link = models.CharField(max_length=100, null=True)
  url = models.CharField(max_length=50, primary_key=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.group_name

class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  group = models.ForeignKey(Group,related_name='posts',null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey('Post',related_name='comments')
  author=models.ForeignKey('auth.User',on_delete=models.PROTECT)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.text
