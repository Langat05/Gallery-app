from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return  render(request, 'all/dashboard.html')

def about(request):
    return  render(request, 'all/about.html')  

def images(request):
    images = Image.objects.all()
    return  render(request, 'all/images.html',{'images':images}) 

    