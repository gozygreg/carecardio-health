from django.contrib import admin
from .models import Clincian, Patient, Appointment


class ClincianAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "email")


class PatientAdmin(admin.ModelAdmin):
    list_display = ("name",)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("clinician", "patient", "date", "time",
                    "year")  # Add "year" to the list

    # Add search fields for patient and clinician names
    search_fields = ("patient__name", "clinician__name")


admin.site.register(Clincian, ClincianAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
