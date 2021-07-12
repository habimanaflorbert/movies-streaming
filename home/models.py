from django.db import models
from django.db import models
from django.contrib.auth.models import User,auth
from django.template.defaultfilters import slugify 
from django.urls import reverse

# Create your models here.
class Admin(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    TypeAccount=models.CharField(max_length=54,default='Admin')
    Created_at=models.DateTimeField(auto_now_add=True)

class Clients(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    TypeAccount=models.CharField(max_length=54,default='Person Account')
    age=models.CharField(max_length=255)
    Created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)


class Category(models.Model):
    title=models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Videos(models.Model):
    title=models.CharField(max_length=255)
    categ=models.ForeignKey(Category, on_delete=models.CASCADE)
    desc=models.TextField()
    category=models.CharField(max_length=255)
    image=models.FileField(upload_to='Covers')
    Created_at=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)