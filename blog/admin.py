from django.contrib import admin
from .models import Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["title", "author", "date_posted"]

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['name', 'message']


admin.site.register(Comment, CommentAdmin)

