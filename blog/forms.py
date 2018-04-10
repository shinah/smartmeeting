# -*- coding: utf-8 -*-
from django import forms
from .models import Post,Group,Comment
from django.contrib.auth.models import User

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_name','group_link',)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

		
class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password']
    widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Password'}),
        }

class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
    widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Name'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Password'}),
        }