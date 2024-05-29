from django.shortcuts import render
from administration_bit.models import Notification

# Create your views here.


def index(request):
    context = {
        'notifications': Notification.objects.all()
    }
    return render(request, 'home/index.html', context=context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')