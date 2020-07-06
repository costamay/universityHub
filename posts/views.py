from django.shortcuts import render, redirect, get_object_or_404, reverse
from posts.models import *

from .forms import *

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
    context = {
        'projects': projects
    }
    
    return render(request, 'project.html', context)

def singleproject(request, id):
    post = get_object_or_404(ProjectPost, id=id)
    print(post)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
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
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return reverse(reverse('post-detail', kwargs={
                'id': form.instance.id
            } ))
    context = {
        'title': title,
        'form': form
    }
    
    return render(request, 'post_create.html', context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(ProjectPost, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid:
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
