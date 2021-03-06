#-*- coding: utf-8 -*-
import json
import urllib
import urllib.request
import urllib.parse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext

#모델 및 폼
from .models import Post, Group, Vote, Document, Task, Chat
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login, authenticate
from .forms import PostForm, UserForm, LoginForm, GroupForm, VoteForm,doVoteForm, DocumentForm, TaskForm
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
            #group.url = group.group_link[28:40]
            #group.url = group.group_link[45:57]#파이썬애니웨어
            group.url = group.group_link[30:42]#서버배포
            group.published_date = timezone.now()
            group.save()
            user = get_object_or_404(User,username=request.user)
            #group2 = get_object_or_404(Group, url = group.url)
            group.user.add(user)
            return redirect('dic:group', url=group.url)
    else:
        form = GroupForm()
    return render(request, 'blog/group_make.html',{'a':a, 'form':form})

def group_list(request):
    groups = Group.objects.filter(user=request.user)
    return render(request,'blog/group_list.html', {'groups':groups})

def group(request,url):
    group = get_object_or_404(Group, url = url)
    #if group.user.all().find != request.user:
            #return redirect('group_invitation/', url= group.url)
    return render(request,'blog/group.html',{'group':group})

def group_invitation(request, url):
    group = get_object_or_404(Group, url = url)
    try:
        user = User.objects.get(username=request.user)
        group.user.add(user)
    except User.DoesNotExist:
        redirect('/sign_in')

    return render(request, 'blog/group_invitation.html',{'group':group})

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

def vote_new(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.published_date = timezone.now()
            vote.post = post
            vote.save()
            #return redirect('dic:vote',pk  =post.pk,id = vote.id)
            return redirect('dic:vote_list',pk=post.pk)

    else:
        form = VoteForm()
    return render(request,'blog/vote_edit.html',{'post':post,'form':form})
    
def vote_list(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/vote_list.html', {'post': post})

def vote_result(request,id):
    vote = get_object_or_404(Vote,id=id)
    return render(request,'blog/vote_result.html',{'vote':vote})

def vote(request,pk,id):
    post = get_object_or_404(Post,pk=pk)
    vote = get_object_or_404(Vote,id=id)
    if 'value1' in request.POST:
        form = doVoteForm(request.POST)
        dovote = form.save(commit=False)
        dovote.id = vote.id
        dovote.vote_title = vote.vote_title
        dovote.vote_text = vote.vote_text
        dovote.vote_num = vote.vote_num
        dovote.post = vote.post
        dovote.agree = vote.agree+1
        dovote.disagree = vote.disagree
        dovote.nothing = vote.nothing
        dovote.num = vote.num+1
        dovote.save()
        user = get_object_or_404(User,username=request.user)
        dovote.user.add(user)
        return redirect('dic:vote_list',pk=post.pk)
    elif 'value2' in request.POST:
        form = doVoteForm(request.POST)
        if form.is_valid():
            dovote = form.save(commit=False)
            dovote.id = vote.id
            dovote.vote_title = vote.vote_title
            dovote.vote_text = vote.vote_text
            dovote.vote_num = vote.vote_num
            dovote.post = vote.post            
            dovote.disagree = vote.disagree+1
            dovote.agree = vote.agree
            dovote.nothing = vote.nothing
            dovote.num = vote.num+1
            dovote.save()
            user = get_object_or_404(User,username=request.user)
            dovote.user.add(user)
            return redirect('dic:vote_list',pk=post.pk)
    elif 'value3' in request.POST:
        form = doVoteForm(request.POST)
        if form.is_valid():
            dovote = form.save(commit=False)
            dovote.id = vote.id
            dovote.vote_title = vote.vote_title
            dovote.vote_text = vote.vote_text
            dovote.vote_num = vote.vote_num
            dovote.post = vote.post 
            dovote.nothing = vote.nothing+1
            dovote.disagree = vote.disagree
            dovote.agree = vote.agree
            dovote.num = vote.num+1
            dovote.save()
            user = get_object_or_404(User,username=request.user)
            dovote.user.add(user)
            return redirect('dic:vote_list',pk=post.pk)
    else:
        form = doVoteForm()

    return render(request,'blog/vote.html',{'post':post,'vote':vote,'form':form})

def file_new(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            newdoc = form.save(commit=False)
            newdoc.docfile = request.FILES['docfile']
            newdoc.post = post
            newdoc.user = request.user
            newdoc.published_date=timezone.now()
            newdoc.save()
            return redirect('dic:file_list2',pk=post.pk)
    else:
        form = DocumentForm()
    return render(request,'blog/file_new.html',{'post':post,'form':form})

'''def file_list(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/file_list.html',{'post':post})'''

def file_list2(request,pk):
    post = get_object_or_404(Post,pk=pk)
    documents = post.files.all()
    return render(request,'blog/file_list2.html',{'post':post,'documents':documents})

def file_list3(request,pk):
    post = get_object_or_404(Post,pk=pk)
    documents = post.files.all().order_by('-published_date')
    return render(request,'blog/file_list3.html',{'post':post,'documents':documents})

def task_new(request,pk):
    post = get_object_or_404(Post,pk=pk)
    group = post.group
    users = group.user.all() 

    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.post = post
            task.user = request.user
            task.save()
            #return redirect('/')
            return redirect('dic:task_list', pk=post.pk)
    else:
        form = TaskForm()
    return render(request,'blog/task_new.html',{'post':post,'form':form, 'users':users})

def task_list(request, pk):
    post = get_object_or_404(Post,pk=pk)
    group = post.group
    users = group.user.all()
    tasks = Task.objects.filter(post = post).order_by('deadline')
    return render(request, 'blog/task_list.html', {'post': post, 'users':users, 'tasks':tasks})


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

def chat_room(request,pk):
    post = get_object_or_404(Post,pk=pk)
    chats = Chat.objects.filter(post=post)
    ctx = {
        'chat_room': 'active',
        'chat': chats,
        'post': post,
    }
    return render(request, 'blog/chat_room.html', ctx)
    
def posting(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        print('Our value = ', msg)
        chat_message = Chat(user=request.user, message=msg, post=post)
        msg = chat_message.user.username+": "+msg
        chat_message = Chat(user=request.user, message=msg, post=post)
        if msg != '':
            chat_message.save()
        return JsonResponse({'msg': msg, 'user': chat_message.user.username})
    else:
        return HttpResponse('Request must be POST.')


def messages(request):
    chat = Chat.objects.all()
    return render(request, 'blog/messages.html', {'chat': chat})