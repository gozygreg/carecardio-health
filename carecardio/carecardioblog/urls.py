from django.urls import path
from . import views


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
]
