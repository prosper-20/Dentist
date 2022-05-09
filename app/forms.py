from django import forms
from .models import Appointment, Contact, Newsletter, Quote


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

        fields = ["usermail"]


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote

        fields = ["quote_name", "email", "phone", "message"]