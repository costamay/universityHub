from django.shortcuts import render, redirect, get_object_or_404, reverse
from posts.models import *
from account.models import Account
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from .forms import *
from account.forms import *

PROJECTS_PER_PAGE = 20
def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def projectList(request):
    projects = ProjectPost.objects.all()
    
    page = request.GET.get('page', 1)
    projects_paginator = Paginator(projects, PROJECTS_PER_PAGE)
    
    try:
        projects = projects_paginator.page(page)
    except PageNotAnInteger:
        projects = projects_paginator.page(PROJECTS_PER_PAGE)
    except EmptyPage:
        projects = projects_paginator.page(projects_paginator.num_pages)
    context = {
        'projects': projects
    }
    
    return render(request, 'project.html', context)

def singleproject(request, id):
    post = get_object_or_404(ProjectPost, id=id)
    print(post.id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.post = post
            form.instance.project_posted = post
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': post.id
            }))
    
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'singleproject.html', context)

def post_project(request):
    title = 'Post your project here'
    form = PostForm(request.POST or None, request.FILES or None)
    user = request.user

    if not user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        if form.is_valid():
            obj= form.save(commit=False)
            author = user.author
            obj.author = author
            obj.save()
            return redirect("post-list")
            
    context = {
        'title': title,
        'form': form
    }
    
    return render(request, 'post_create.html', context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(ProjectPost, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    user = request.user
    
    if post.author != user:
        return HttpResponse('You are not the author of that project.')
    
    if request.method == 'POST':
        if form.is_valid:
            author = Account.objects.filter(email=user.email).first()
            form.instance.author = author
            form.save()
            return reverse(reverse('post-detail', kwargs={
                'id': form.instance.id
            } ))
    context={
        'title': title,
        'form': form
    }
    return render(request, 'post_create.html', context)


def account_view(request):
    if request.method == 'POST':
       
        author_form = AuthorUpdateForm(request.POST, request.FILES, instance=request.user.author)
        form = AccountUpdateForm(request.POST, instance=request.user)
        
        if author_form.is_valid() or form.is_valid():
            author_form.save()

         
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
           
            
            
    else:
        
        author_form = AuthorUpdateForm(instance=request.user.author)
        form = AccountUpdateForm(
            initial = {
                "email": request.user.email,
                "username": request.user.username
            }
        )
        
    context = {
        'author_form': author_form,
        'success_mess': 'Updated',
        'success_message' : 'Updated',
        'account_form' : form
        
    }
    project_posts = ProjectPost.objects.filter(author=request.user.author)
    context['project_posts'] = project_posts
    return render(request, 'account/account.html', context)