from django.contrib.auth import models
from django.shortcuts import render, redirect
from blogs.models import Blog
from about_us.models import About
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_posts = Blog.objects.filter(is_featured = True, status="Published").order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status="Published").order_by('-updated_at')
    about = About.objects.get()

    context = {
        "featured_posts" : featured_posts,
        "posts" : posts,
        "about" : about ,
    }

    return render(request, 'home.html', context)


def register(request):
    if request.method == "POST" :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')  
        else:
            print(form.errors)
    else :
        form = RegistrationForm()

    context = {
        'form' : form
    }
    return render(request, "register.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(request, username = username, password=password)

            if user is not None:
                auth.login(request,user)

            return redirect('home')
        else:
            messages.error("Invalid Credentials")
    else:
        form = AuthenticationForm()

    context = {
        "form" : form
    }
    return render(request, "login.html", context)

def logout(request):
    auth.logout(request)
    return redirect('home')