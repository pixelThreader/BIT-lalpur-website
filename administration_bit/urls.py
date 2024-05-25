from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="administration"),
    path("placements/", views.palcements, name="administration"),
]