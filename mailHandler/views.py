from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse({'Status': "200"})


def student_to_BIT(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse({'Status': "200"})