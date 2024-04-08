from django.shortcuts import render, redirect
from django.db.models import Q
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

def blogs(request, slug):
    single_blog = Blog.objects.get(status="Published", slug=slug)

    context = {
        'single_blog' :single_blog,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    # print(f"keyword ----> : -{keyword}-")
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |
                                Q(blog_body__icontains=keyword), status="Published")
        
    context = {
        'blogs' : blogs,
        'keyword' : keyword
    }
    return render(request, 'search.html', context)