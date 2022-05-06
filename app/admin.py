from django.contrib import admin
from .models import Services, Appointment, Contact

# Register your models here.

admin.site.register(Services)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'department']


admin.site.register(Appointment, AppointmentAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]

admin.site.register(Contact, ContactAdmin)
