from django.urls import path

from blog.models import Post
from . import views
from .views import PostListView,PostDetailView, detail, PostCommentView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("<slug:slug>/", detail, name="detail"),
    path('<slug:slug>/comment/', PostCommentView, name="post_comments"),

    # path("<slug:slug>/", PostDetailView.as_view(), name="post_detail")
]