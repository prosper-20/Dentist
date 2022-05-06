from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default='')
    image = models.ImageField(upload_to="post_images")
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs): # < here
        self.slug = slugify(self.title)
        super(Post, self).save()

