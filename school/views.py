from django.shortcuts import render
from django.http import HttpResponse


def HomePage(request):
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

# def ContactPage(request):
#     return  
