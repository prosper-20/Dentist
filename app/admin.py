from django.contrib import admin
from .models import Services, Appointment

# Register your models here.

admin.site.register(Services)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'department']


admin.site.register(Appointment, AppointmentAdmin)
