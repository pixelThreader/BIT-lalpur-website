from django.shortcuts import render
from administration_bit.models import Notification
import datetime

# Create your views here.

def index(request):
    context = {
        'notifications': Notification.objects.filter(is_valid=True),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/index.html', context=context)

def to_user(request):
    context = {
        'notifications': Notification.objects.filter(is_valid=True),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/to_user.html', context=context)