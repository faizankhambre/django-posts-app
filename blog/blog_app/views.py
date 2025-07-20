from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from . import forms

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def posts(req):
    posts = Post.objects.all().order_by('-created_at')
    return render(req, 'posts.html', {'posts': posts})

@login_required(login_url='user_login')
def new_post(req):
    if req.method == 'POST':
        form = forms.CreatePost(req.POST, req.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = req.user
            newpost.save()
            return redirect('posts')
    else:
        form = forms.CreatePost()
    return render(req, 'new_posts.html', {'form': form})

def post_page(req, slug):
    post = Post.objects.get(slug=slug)
    return render(req, 'single_post.html', {'post': post})