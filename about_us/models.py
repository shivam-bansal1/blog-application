from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=50)
    about_description = models.CharField(max_length=200)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.about_heading
    

class SocialLink(models.Model):
    platform = models.CharField(max_length=25, unique=True)
    link = models.URLField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform