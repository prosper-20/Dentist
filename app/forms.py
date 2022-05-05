from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment

        fields = ["department", "name", "email", "date", "time", "phone"]