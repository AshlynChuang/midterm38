from django.shortcuts import render, redirect
from mysite.models import Book
from mysite import models
from django.http import HttpResponse
from datetime import datetime
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')

def homepage(request):
    posts = Book.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    post = Book.objects.get(slug=slug)
    return render(request, 'post.html', locals())

class SignLogView(View):
    def get(self, request):
        return render(request, 'signlog.html')
    
class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 登入驗證邏輯，如果登入成功...

        return redirect('home')
    
class RegisterView(View):
    def post(self, request):
        fullname = request.POST.get('fullname')
        username = request.POST.get('username2')
        password = request.POST.get('password2')
        confirm_password = request.POST.get('confirm_password')

        # 註冊驗證邏輯，如果註冊成功...

        return redirect('home')

def testme(request):
    return HttpResponse("hello world")

'''def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    for counter, post in enumerate(posts):
        posts_lists.append(f'No. {counter}-{post} <br>')
        return HttpResponse(posts_lists) '''