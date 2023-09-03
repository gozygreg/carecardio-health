from django.urls import path
from . import views


urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
    path("module/<int:module_id>/", views.module_detail, name="module_detail"),
    path("enroll/<int:course_id>/", views.enroll_course, name="enroll_course"),
]
