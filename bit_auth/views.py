from django.shortcuts import render, redirect
from django.contrib.auth import logout
import datetime

# Create your views here.

def login__(request):
    cont = {
        'year': datetime.datetime.now().year
    }
    return render(request, 'auth/login.html', context=cont)

def signup(request):
    return render(request, 'auth/sign_up.html')

def password_reset(request):
    return render(request, 'auth/reset_passwd.html')

def password_forget(request):
    return render(request, 'auth/forget_passwd.html')

def logout_bit(request):
    logout(request)
    return redirect('home')