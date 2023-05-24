from django.urls import path
from . import views


urlpatterns = [
    path('schedule/', views.schedule_appointment, name='schedule_appointment'),
    path('list/', views.appointments_list, name='appointments_list'),
    path('doctors/', views.available_doctors, name='available_doctors'),
]
