# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Group(models.Model):
  group_name = models.CharField(max_length=100)
  group_link = models.CharField(max_length=100, null=True)
  url = models.CharField(max_length=50, primary_key=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  user = models.ManyToManyField('auth.User',related_name='user', default=None)

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

#class Comment(models.Model):
#  post = models.ForeignKey(Post,related_name='comments',null=True)
#  author=models.ForeignKey('auth.User',on_delete=models.PROTECT)
#  text = models.TextField()
#  created_date = models.DateTimeField(default=timezone.now)
#  published_date = models.DateTimeField(blank=True, null=True)

#  def __str__(self):
#    return self.text

class Vote(models.Model):
  post = models.ForeignKey(Post,related_name='votes',null=True)
  user=models.ManyToManyField('auth.User',related_name='vote_user', default=None)
  vote_title = models.CharField(max_length=200)
  vote_text = models.TextField()
  vote_num = models.IntegerField(null=True)
  num = models.IntegerField(default=0)
  agree = models.IntegerField(default=0)
  disagree = models.IntegerField(default=0)
  nothing = models.IntegerField(default=0)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  def __str__(self):
    return self.vote_title

class doVote(models.Model):
  vote = models.ForeignKey(Vote,related_name='doVote')
  num = models.IntegerField(default=0)
  agree = models.IntegerField(default=0)
  disagree = models.IntegerField(default=0)
  nothing = models.IntegerField(default=0)

class Task(models.Model):
  post = models.ForeignKey(Post,related_name='takes',null=True)
  user = models.ForeignKey('auth.User',related_name='users')
  thisUser = models.TextField(null=True)
  toDo = models.TextField(null = False)
  deadline = models.TextField()
  #deadline = models.DateField(default=datetime.datetime.now)
