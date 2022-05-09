from re import sub
from telnetlib import DO
from django.shortcuts import redirect, render
from django.http import HttpResponse

from app.models import Appointment, Contact, Doctor, Newsletter, Quote
from blog.models import Post
from .forms import AppointmentForm, NewsletterForm
from django.contrib import messages
# Create your views here.


def home(request):
    posts = Post.objects.all()
    my_post = Post.objects.all()[:2]
    doctors = Doctor.objects.all()
    if request.method == "POST":
        name = request.POST.get("quote_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST["message"]
        # You added this for the subscription to news letter
        # usermail = request.POST.get("usermail")

        quote = Quote.objects.create(quote_name=name, email=email, phone=phone, message=message)
        quote.save()
        # usermail = Newsletter.objects.create(usermail=usermail)
        # usermail.save()
        messages.success(request, "Your quote will be sent to your email soon")
        return redirect("index")
    
    else:
        return render(request, 'app/home.html', {"doctors": doctors, "posts": posts, "my_post":my_post})

def about(request):
    my_post = Post.objects.all()[:2]
    return render(request, 'app/about.html', {"my_post": my_post})

def service(request):
    my_post = Post.objects.all()[:2]
    return render(request, 'app/service.html', {"my_post": my_post})


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
        return render(request, 'app/home.html')


def doctors(request):
    return render(request, 'app/doctors.html')


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        new = Contact.objects.create(name=name,
        email=email, subject=subject, message=message)
        new.save()
        messages.success(request, f"Hi {name}, your message has been received. Expect a reply soon!")
        return redirect('contact')
    else:
        return render(request, 'app/contact.html')


# You added this for the make an appointment on the navbar
def appointment_2(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        phone = request.POST['phone']

        new = Appointment.objects.create(name=name,
        email=email, date=date, time=time, phone=phone)
        new.save()
        messages.success(request, f"Hi {name}, your appointment has been scheduled!")
        return redirect("/")
    else:
        return render(request, 'app/home.html')



def newsletter(request):
    if request.method == "POST":
        usermail = request.POST['usermail']

        new = Newsletter.objects.create(usermail=usermail)
        new.save()
        return redirect("/")

    else:
        return render(request, 'app/home.html')



def newsletter2(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            return redirect("/")
    else:
        form = NewsletterForm()
    context = {
        "form": form,
    }
    return render(request, "app/new.html", context)


def quote(request):
    if request.method == "POST":
        name = request.POST["quote_name"]
        email = request.POST["email"]
        phone = request.POST.get["phone"]
        message = request.POST["message"]

        quote = Quote.objects.create(quote_name=name, email=email, phone=phone, message=message)
        quote.save()
        messages.success(request, "Your quote will be sent to your email soon")
        return redirect("index")
    else:
        return render(request, "app/home.html")


