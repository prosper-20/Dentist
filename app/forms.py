from django import forms
from .models import Appointment, Contact, Newsletter


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment

        fields = ["department", "name", "email", "date", "time", "phone"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = ["name", "email", "subject", "message"]


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter

        fields = ["email"]