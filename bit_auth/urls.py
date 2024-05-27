from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login__, name="login"),
    path("register/", views.signup, name="signup"),
    path("password-reset/", views.password_reset, name="password_reset"),
    path("password-forget/", views.password_forget, name="password_reset_sent"),
    path("logout/", views.logout_bit, name="logout"),
]