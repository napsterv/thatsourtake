from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Post
# Create your views here.

# class PostView(View):
# 	model = Post
# 	context_object_name = 'articles'
# 	template_name = 'index.html'

class PostView(TemplateView):
	template_name = "index.html"
	queryset = Post.objects.all()
	context_object_name = 'articles'