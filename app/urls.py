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
    path('appointment/', views.appointment, name="appointment"),
    path('appoint/', views.appointment_2, name="appoint"),
    path('doctors/', views.doctors, name="doctors"),
    path("", views.newsletter, name="home"),
    path("tester/", views.newsletter2, name="tester"),
    path("", views.quote, name="quote")
]