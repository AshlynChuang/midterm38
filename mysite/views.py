from django.shortcuts import render
from mysite.models import Book
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

def homepage(request):
    posts = Book.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    post = Book.objects.get(slug=slug)
    return render(request, 'post.html', locals())

def testme(request):
    return HttpResponse("hello world")

'''def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    for counter, post in enumerate(posts):
        posts_lists.append(f'No. {counter}-{post} <br>')
        return HttpResponse(posts_lists) '''