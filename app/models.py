from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="service_images")

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name
