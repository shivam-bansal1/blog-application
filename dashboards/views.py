from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

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

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category':category,
    }
    return render(request, "dashboard/edit_category.html", context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def post(request):
    posts = Blog.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'dashboard/post.html', context)

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            title = form.cleaned_data['title']
            print(title)
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()

            return redirect('posts')
        else:
            print("Invalid Form")
            print(form.errors)

    form = BlogPostForm()
    context = {
        'form':form
    }

    return render(request, "dashboard/add_post.html", context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()

            return redirect('posts')
        else:
            print(form.errors)

    form = BlogPostForm(instance=post)

    context = {
        'form':form,
        'post':post,
    }

    return render(request, "dashboard/edit_post.html", context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')