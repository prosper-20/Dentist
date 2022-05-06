from django.urls import path

from blog.models import Post
from . import views
from .views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home")
]