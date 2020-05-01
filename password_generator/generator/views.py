from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home_old(request):
    return HttpResponse("Hello there friend!")

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    #thispassword = 'test'
    characters = 'abcdefghijklmnopqrstuvwxyz'
    
    # password
    length = int(request.GET.get('length',12))
    
    # uppercase values 
    if request.GET.get('uppercase'):
        characters+=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # adding numbers
    if request.GET.get('numbers'):
        characters+=('1234567890')
    
    # adding special characters
    if request.GET.get('special'):
        characters+=('~!@#$%^&*(')
    
    
    
    thispassword = ''.join(random.sample(characters, length))
    
    
    return render(request, 'generator/password.html',{'password': thispassword})