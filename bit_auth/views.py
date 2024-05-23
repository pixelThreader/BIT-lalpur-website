from django.shortcuts import render

# Create your views here.

def login_admin_bit(request):
    return render(request, 'bit_auth/login_admin_bit.html')

def login_teachers(request):
    return render(request, 'bit_auth/login_teachers.html')

def signup_teachers(request):
    return render(request, 'bit_auth/signup_teachers.html')

def password_reset(request):
    return render(request, 'bit_auth/password_reset.html')

def password_forget(request):
    return render(request, 'bit_auth/password_reset.html')

def logout_bit(request):
    return render(request, 'bit_auth/logout_bit.html')