from django.urls import path
from . import views


app_name = "uploaderapp"
urlpatterns = [
    path("", views.home),
    path("upload/", views.upload),
]
