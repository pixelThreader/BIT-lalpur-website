from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mail"),
    path("studentBIT/", views.student_to_BIT, name="student_to_BIT"),
]
