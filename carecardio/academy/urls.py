from django.urls import path
from . import views

# app_name = 'learning'

urlpatterns = [
    # path('', views.video_list, name='video_list'),
    path('<int:course_id', views.course_detail, name='course_detail'),
    # path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    path('videos/<int:module_id>/', views.module_detail, name='module_detail'),
]
