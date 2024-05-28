from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'administrations/index.html')

def palcements(request):
    return render(request, 'administrations/palcements.html')

def departments(request):
    return render(request, 'administrations/departments.html')

def department_course(request, course):
    print(course)
    return render(request, 'administrations/department_course.html')

def faq(request):
    return render(request, 'administrations/faq.html')
