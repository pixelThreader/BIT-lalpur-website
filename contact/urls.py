from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="contact"),
    path("to/", views.to_user, name="to_user"),
]