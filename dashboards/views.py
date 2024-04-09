from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    categories_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'categories_count' : categories_count,
        'blogs_count' : blogs_count,
    }

    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoryForm(request.POST)

    context = {
        'form' : form
    }

    return render(request, 'dashboard/add_category.html', context)