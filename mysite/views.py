from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from mysite.models import Book
from mysite import models
from django.http import HttpResponse
from datetime import datetime
from django.views import View
from django.contrib import messages
import os

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
    
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list.html')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 將 'home' 替換為你的首頁視圖的名稱
    else:
        form = UserCreationForm()
    
    template_path = os.path.join(settings.BASE_DIR, 'midterm38/templates/registration/register.html')
    print(f'Template Path: {template_path}')
    
    return render(request, 'registration/register.html', {'form': form})

def testme(request):
    return HttpResponse("hello world")

def login_view(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                logger.debug(f'Successfully logged in: {user.username}')
                # 登入成功後將頁面導向到 home.html
                return redirect('book_list')
            else:
                messages.error(request, 'Invalid username or password.')
                logger.warning('Login failed: Invalid username or password.')



'''def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    for counter, post in enumerate(posts):
        posts_lists.append(f'No. {counter}-{post} <br>')
        return HttpResponse(posts_lists) '''