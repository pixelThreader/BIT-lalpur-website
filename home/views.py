from django.shortcuts import render
from administration_bit.models import Notification
import datetime

# Create your views here.


def index(request):
    context = {
        'notifications': Notification.objects.filter(is_valid=True),
        'year':  datetime.date.today().year
    }
    return render(request, 'home/index.html', context=context)

def about(request):
    context = {
        'notifications': Notification.objects.filter(is_valid=True),
        'year':  datetime.date.today().year
    }
    return render(request, 'home/about.html', context=context)
