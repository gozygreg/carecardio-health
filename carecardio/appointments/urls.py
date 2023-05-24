from django.urls import path
from . import views


urlpatterns = [
    path('schedule/', views.schedule_appointment, name='schedule_appointment'),
    path('list/', views.appointments_list, name='appointments_list'),
    path('clinician/', views.available_doctors, name='available_clinician'),
]
