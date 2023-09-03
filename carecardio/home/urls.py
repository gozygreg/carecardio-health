from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact_us.html", views.contact_us, name="contact_us"),
    path("about_us.html", views.about_us, name="about_us"),
    path("services.html", views.services, name="services"),
    # path('blog.html', views.post_list, name='blog'),
]
