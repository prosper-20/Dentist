from django import forms
from .models import Appointment, Contact


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment

        fields = ["department", "name", "email", "date", "time", "phone"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fieds = ["name", "email", "subject", "message"]