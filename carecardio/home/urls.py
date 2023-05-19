from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us.html', views.contact_us, name='contact_us'),
]
