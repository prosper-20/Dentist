from django.contrib import admin
from .models import Services, Appointment, Contact, Doctor, Newsletter

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
