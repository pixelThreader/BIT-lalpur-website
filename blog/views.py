from django.shortcuts import render
from administration_bit.models import Notification
import datetime

# Create your views here.

def index(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'blog/index.html', context=context)

def blog(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'blog/blog.html', context=context)

def blog_post(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'blog/blog_post.html', context=context)

def search(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'blog/search.html', context=context)

