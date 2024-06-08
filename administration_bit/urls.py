from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="administration"),
    path("placements/", views.palcements, name="plcements"),
    path("departments/", views.departments, name="departments"),
    path("departments/<str:slug>", views.department, name="department"),
    path("timetable/", views.timetable, name="timetable"),
    path("courses/<str:course>/", views.department_course, name="courses"),
    path("faqs/", views.faq, name="faqs"),
]