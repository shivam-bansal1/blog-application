from django.contrib.auth import models
from django.shortcuts import render
from blogs.models import Blog
from about_us.models import About

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