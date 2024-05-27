from django.shortcuts import render

# Create your views here.

def login__(request):
    return render(request, 'auth/login.html.html')

def signup(request):
    return render(request, 'auth/create_account.html')

def password_reset(request):
    return render(request, 'auth/reset_passwd.html')

def password_forget(request):
    return render(request, 'auth/forget_passwd.html')

def logout_bit(request):
    return 