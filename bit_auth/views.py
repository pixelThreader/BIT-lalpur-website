from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
import datetime
from django.http import Http404

# Create your views here.

def login__(request):
    if request.method == 'POST':
        mhtd = request.POST.get('via-login-method')

        # login via email
        if mhtd == '__email':
            email = request.POST.get('via-email-user')
            passwd = request.POST.get('via-email-passwd')
            who = request.POST.get('via-email-select')
            user = authenticate(request, email=email, password=passwd, who=who) 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('Wrong Email or Password')
                raise Http404
            
        # login via email
        if mhtd == '__username':
            username = request.POST.get('via-username-user')
            passwd = request.POST.get('via-username-passwd')
            who = request.POST.get('via-username-select')
            user = authenticate(request ,username=username, password=passwd, who =who)
            if user is not None:
                login(request, user)
                return redirect('about')
            else :
                print('Wrong Email or Password')
                raise Http404

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
    return