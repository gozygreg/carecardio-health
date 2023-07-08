from django.urls import path
from . import views

# app_name = 'learning'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
]
