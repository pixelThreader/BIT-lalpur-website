from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="files"),
    path("files/", views.files, name="files"),
    path("files/preview/", views.preview, name="upload"),
    path("download/", views.download, name="download"),
]