from django.shortcuts import render
from django.http import JsonResponse
from administration_bit.models import Notification
from .sendmail import send_single_mail
import datetime

# Create your views here.

def index(request):
    context = {
        'notifications': Notification.objects.filter(is_valid=True),
        'year':  datetime.date.today().year
    }
    return render(request, 'home/contact.html', context=context)

def to_user(request):

    context = send_single_mail()

    # if request.method=='POST':
    #     name = request.POST.get('sender-name')
    #     from_email = request.POST.get('sender-mail')
    #     to_email = request.POST.get('reciver-mail')
    #     title = request.POST.get('mail-header')
    #     description = request.POST.get('mail-body')

    # context = {
    #     'notifications': Notification.objects.filter(is_valid=True),
    #     'year':  datetime.date.today().year
    # }
    return JsonResponse(context)