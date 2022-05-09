from django.contrib import admin
from .models import Services, Appointment, Contact, Doctor, Newsletter, Quote

# Register your models here.

admin.site.register(Services)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'department']


admin.site.register(Appointment, AppointmentAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]

admin.site.register(Contact, ContactAdmin)

class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ["name", "job"]


admin.site.register(Doctor, DoctorAdmin)


admin.site.register(Newsletter)


class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ["quote_name", "email", "phone", "message"]


admin.site.register(Quote, QuoteAdmin)