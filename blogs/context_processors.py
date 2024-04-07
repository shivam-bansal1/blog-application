from .models import Category
from about_us.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    
    return {'categories':categories}

def get_social_links(request):
    social_links = SocialLink.objects.all()

    return {'social_links':social_links}