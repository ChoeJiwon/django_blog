from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects    #QuerySet #method
    return render(request, 'home.html', {'blogs':blogs})
