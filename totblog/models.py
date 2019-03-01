from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

STATUS_CHOICES = (('d', 'Draft'), ('p', 'Published'), ('wd', 'Withdrawn'))

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=15)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    featured_Post = models.BooleanField(default=True)
    featured_Image = models.ImageField(upload_to='assets/images')
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='d')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    source = models.URLField(null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = False, default = timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=15)
    body = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    banner_Image = models.ImageField(upload_to='assets/images')

    def __str__(self):
        return self.title
