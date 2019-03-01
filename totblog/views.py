from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostView(ListView):
	queryset = Post.objects.all()
	#context_object_name = 'posts'
	template_name = 'index.html'