import json
import urllib
import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext

#모델 및 폼
from .models import Post, Group
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import PostForm, UserForm, LoginForm, GroupForm, CommentForm

from django.utils import timezone

from .group import *



def index(request):
	isuser = 0
	return render(request, 'blog/index.html', {'isuser':isuser})

def group_make(request):
    ran = Random_make()
    a = ran.random_url()
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.url = group.group_link[28:40]#변경부분
            group.published_date = timezone.now()
            group.save()
            return redirect('dic:group',url=group.url)
    else:
        form = GroupForm()
    return render(request, 'blog/group_make.html',{'a':a, 'form':form})

def group_list(request):
    groups = Group.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/group_list.html', {'groups':groups})

def group(request,url):
    group = get_object_or_404(Group, url = url)
    return render(request,'blog/group.html', {'group':group})

def post_new(request,url):
    group = get_object_or_404(Group, url = url)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.group = group
            post.save()
            return redirect('dic:group', url=group.url)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_list(request):
	posts = Post.objects.select_Related('group')
	return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def chat_room(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('dic:chat_room',pk = post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/chat_room.html',{'post':post,'form':form})

def signup(request):
    if request.method == "POST":
    	form = UserForm(request.POST)
    	print(form)
    	if form.is_valid():
    		new_user = User.objects.create_user(**form.cleaned_data)
    		login(request, new_user)
    		return redirect('/')
    	else:
    		isuser = 1
    		return render(request, 'blog/sign_up.html', {'form': form, 'isuser':isuser})
    else:
    	isuser = 1
    	form = UserForm()
    	return render(request, 'blog/sign_up.html', {'form': form, 'isuser':isuser})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
        	isuser = 1
        	return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        isuser = 1
        return render(request, 'blog/sign_in.html', {'form': form, 'isuser':isuser})
