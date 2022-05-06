from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


