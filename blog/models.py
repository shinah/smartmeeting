# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
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

  #User모델 확장: user별 그룹 정보 포함.
class User_belong(models.Model):
  user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
  g1 = models.CharField(max_length=100, null=True)
  g2 = models.CharField(max_length=100, null=True)
  g3 = models.CharField(max_length=100, null=True)

  def add(self, group_name):
    if self.g1 is None:
      self.g1 == group_name
    elif self.g2 is None:
      self.g2 == group_name
    elif self.g3 is None:
      self.g3 == group_name
    else:
      return False
