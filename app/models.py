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


DEPARTMENT_CHOICES = [
    ("Teeth Whitening", "Teeth Whitening"),
    ("Teeth Cleaning", "Teeth Cleaning"),
    ("Braces", "Braces"),
    ("Modern Anesthetic", "Modern Anesthetic")

]



    
class Appointment(models.Model):
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(choices=TIME_CHOICES, max_length=100)
