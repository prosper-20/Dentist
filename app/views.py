from django.shortcuts import redirect, render
from django.http import HttpResponse

from app.models import Appointment
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


def appointment_2(request):
    if request.method == "POST":
        name = request.POST['name']
        department = request.POST['department']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        phone = request.POST['phone']

        new = Appointment.objects.create(department=department, name=name,
        email=email, date=date, time=time, phone=phone)
        new.save()
        messages.success(request, f"Hi {name}, your appointment has been scheduled!")
        return redirect("/")
    else:
        form = AppointmentForm()
    
    return render(request, 'app/home.html')


