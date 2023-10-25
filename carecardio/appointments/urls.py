from django.urls import path
from . import views


urlpatterns = [
    path("schedule/", views.schedule_appointment, name="schedule_appointment"),
    path("appointment_success/", views.appointment, name="appointment_success"),
    path("clinician/", views.available_clinician, name="available_clinician"),
]
