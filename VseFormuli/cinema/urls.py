from django.urls import path
from . import views

urlpatterns = [
    path("", views.cinema),
    path("addVideo", views.addVideos)
]