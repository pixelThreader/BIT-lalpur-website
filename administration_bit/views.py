from django.shortcuts import render
from .models import FAQ

# Create your views here.

def index(request):
    return render(request, 'administrations/index.html')

def palcements(request):
    return render(request, 'administrations/placements.html')

def departments(request):
    return render(request, 'administrations/departments.html')

def departments_(request, slug):
    return render(request, 'administrations/departments.html')

def timetable(request):
    return render(request, 'administrations/timetable.html')

def department_course(request, course):
    print(course)
    return render(request, 'administrations/department_course.html')

def faq(request):
    cont = {
        'FAQs': FAQ.objects.all()
    }
    return render(request, 'administrations/faq.html', context=cont)
