from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects    # 전체 데이터
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)     # 해당 데이터
    return render(request, 'detail.html', {'blog_detail' : blog_detail})

def add(request):
    return render(request, 'add.html')

def create(request):    # DB에 form으로 받은 데이터 추가
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))