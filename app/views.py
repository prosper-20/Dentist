from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AppointmentForm
from django.contrib import messages
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

def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            department = form.cleaned_data.get("department")
            email = form.cleaned_data.get("email")
            
            messages.success(request, f"Hi {name}, your appointment has been scheduled!")
            return redirect("/")
    else:
        form = AppointmentForm()
    
    context = {
        "form": form
    }
    return render(request, 'app/appointment.html', context)
