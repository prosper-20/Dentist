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


DEPARTMENT_CHOICES = (
    ("Teeth Whitening", "Teeth Whitening"),
    ("Teeth Cleaning", "Teeth Cleaning"),
    ("Braces", "Braces"),
    ("Modern Anesthetic", "Modern Anesthetic")

)

TIME_CHOICES = (
    ("8:00AM", "8:00AM"),
    ("9:00AM", "9:00 AM"),
    ("10:00AM", "10:00 AM"),
    ("11:00AM", "11:00 AM"),
    ("12:00PM", "12:00 PM"),
    ("1:00PM", "1:00 PM"),
    ("2:00PM", "2:00 PM"),
    ("3:00PM", "3:00 PM"),
    ("4:00PM", "4:00 PM"),
    ("5:00PM", "5:00 PM"),
    ("6:00PM", "6:00 PM"),
    ("7:00PM", '7:00 PM')
)



    
class Appointment(models.Model):
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(choices=TIME_CHOICES, max_length=100)
