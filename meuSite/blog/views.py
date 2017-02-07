from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    var = 'Rubens dos Santos Lopes'
    return render(request, 'blog/post_list.html', {'posts': posts,'var':var})

def novo(request):
    return render(request,'blog/novo.html')

def index(request):
    return render(request,'blog/index.html')
