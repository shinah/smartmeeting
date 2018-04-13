import json
import urllib
import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext

#모델 및 폼
from .models import Post, Group, User_belong
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login, authenticate
from .forms import PostForm, UserForm, UserForm2, LoginForm, GroupForm, CommentForm

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
        form2 = UserForm2()
        if form.is_valid():
            group = form.save(commit=False)
            user_belong = form2.save(commit=False)
            group.url = group.group_link[28:40]#변경부분
            group.published_date = timezone.now()
            group.save()
            user_belong.user = request.user
            user_belong.g1 = group #Group객체로 저장됨.
            user_belong.save()
            return redirect('dic:group', url=group.url)
    else:
        form = GroupForm()
        form2 = UserForm2()
    return render(request, 'blog/group_make.html',{'a':a, 'form':form})

def group_list(request):
    groups = Group.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/group_list.html', {'groups':groups})

def group(request,url):
    group = get_object_or_404(Group, url = url)
    if request.user.is_anonymous:
            return redirect('group_invitation/', url= group.url)
    # 그룹 만든 사람 이외에는 User_belong객체 생성되지 않은 상태
    if User_belong.objects.filter(user = request.user):
        #자기의 그룹 존재, 해당 링크 아닌 경우 404
        user_belong = get_object_or_404(User_belong, user=request.user, g1 = group)
        return render(request,'blog/group.html', {'group':group})
    else:
            return redirect('group_invitation/', url= group.url)

def group_invitation(request, url):
    # user_belong을 새로 만들어야 함.
    group = get_object_or_404(Group, url = url)
    if request.method == "POST":
        form = UserForm2(request.POST)
        if form.is_valid():
            form.save(commit=False)
            thisUrl = get_object_or_404(Group, url = url)
            user_belong = User_belong.objects.create(
                            user = request.user,
                            g1 = thisUrl)
            user_belong.save()
            return render(request,'blog/group.html', {'group':group})
    else:
        form = UserForm2()
    return render(request, 'blog/group_invitation.html', {'form': form})

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
