from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post


def detail(request, slug=None): # < here
    post = get_object_or_404(Post, slug=slug) # < here
    return render(request, 'blog/post_detail.html', {"post": post})



