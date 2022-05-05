from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def service(request):
    return render(request, 'app/service.html')

def contact(request):
    return render(request, 'app/contact.html')

def price(request):
    return render(request, 'app/price.html')

def testimonial(request):
    return render(request, 'app/testimonial.html')
