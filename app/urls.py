from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('service/', views.service, name="service"),
    path('contact/', views.contact, name="contact"),
    path('price/', views.price, name="price"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('apointment/', views.appointment, name="appointment")
]