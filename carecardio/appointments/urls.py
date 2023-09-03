from django.urls import path
from . import views


urlpatterns = [
    path("schedule/", views.schedule_appointment, name="schedule_appointment"),
    path("appointment.html", views.appointment, name="appointment"),
    path("clinician/", views.available_clinician, name="available_clinician"),
]
