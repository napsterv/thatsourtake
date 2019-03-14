from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Post
# Create your views here.




class PostView(ListView):
	template_name = "index.html"
	model = Post
	context_object_name = 'posts'
	#paginate_by = '2'