from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'apptemp2/test2.html')

def link1(request):
    return render(request, 'apptemp2/test2.1.html')

def link2(request):
    return render(request, 'apptemp2/test2.2.html')

def link3(request):
    return render(request, 'apptemp2/test2.3.html' )

def link4(request):
    return render(request, 'apptemp2/test2.4.html')
