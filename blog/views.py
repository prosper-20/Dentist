from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    my_post = Post.objects.all()[:2]
    extra_content = {"my_post": Post.objects.all()[:2]}


class PostDetailView(DetailView):
    model = Post


def detail(request, slug=None): # < here
    post = get_object_or_404(Post, slug=slug) # < here
    if request.method == "POST":
        name = request.POST["name"]
        body = request.POST["body"]

        new = Comment.objects.create(post=post, name=name, body=body)
        new.save()
        messages.success(request, "Comment saved")
        return redirect("/")
        
    else:

        return render(request, 'blog/post_detail.html', {"post": post})


# class PostCommentView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = CommentForm
    # success_url = "/"
    template_name = "blog/post_comment_form.html"

    # def form_valid(self, form):
    #     form.instance.name = self.request.user
    #     form.instance.post_id = self.kwargs['pk']
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.kwargs['slug']})


# def PostCommentView(request, slug=None):
#     post = get_object_or_404(Post, slug=slug)
#     if request.method == "POST":
#         name = request.POST["name"]
#         body = request.POST["body"]

#         new = Comment.objects.create(post=post, name=name, body=body)
#         new.save()
#         messages.success(request, "Comment saved")
#         return redirect("/")
    
#     else:
#         return render(request, "blog/post_detail.html")






