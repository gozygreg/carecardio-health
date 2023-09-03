from django.contrib import admin
from .models import Clincian, Patient, Appointment


class ClincianAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PatientAdmin(admin.ModelAdmin):
    list_display = ("name",)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("clinician", "patient", "date", "time")


admin.site.register(Clincian, ClincianAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
