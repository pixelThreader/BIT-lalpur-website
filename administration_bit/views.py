from django.shortcuts import render
from .models import FAQ
from administration_bit.models import Notification
import datetime

# Create your views here.

def index(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'administrations/index.html', context=context)

def palcements(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'administrations/placements.html', context=context)

def departments(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'administrations/departments.html', context=context)

def department(request, slug):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year,
        'tit': slug
    }
    return render(request, 'administrations/department_course.html', context=context)

def timetable(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year
    }
    return render(request, 'administrations/timetable.html', context=context)

def department_course(request, course):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year,
        'FAQs': FAQ.objects.all()
    }
    print(course)
    return render(request, 'administrations/department_course.html', context=context)

def faq(request):
    context = {
        'notifications': Notification.objects.all(),
        'year':  datetime.date.today().year,
        'FAQs': FAQ.objects.all()
    }
    return render(request, 'administrations/faq.html', context=context)
