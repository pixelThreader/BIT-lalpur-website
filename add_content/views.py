from django.shortcuts import render
from administration_bit.models import Notification
import datetime

# Create your views here.

def index(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/index.html', context=context)

def content_faculty_upload(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/faculty_upload.html', context=context)

def notification(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/notification.html', context=context)

def notice(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/notice.html', context=context)

def gallery(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'add_content/gallery.html', context=context)

