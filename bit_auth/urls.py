from django.urls import path
from . import views

urlpatterns = [
    path("login/admin/", views.login_admin_bit, name="login_admin_bit"),
    path("login/", views.login_teachers, name="login_teachers"),
    path("register/", views.signup_teachers, name="register_teachers"),
    path("logout/", views.logout_bit, name="logout"),
]