from django.contrib.auth import models
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')