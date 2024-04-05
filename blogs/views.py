from django.shortcuts import render, redirect
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id) :
    try:
        posts = Blog.objects.filter(status="Published", category=category_id)
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')
    
    context = {
        'posts' : posts ,
        'category' : category,
    }

    return render(request, "posts_by_category.html", context)