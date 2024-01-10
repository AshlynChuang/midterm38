"""
URL configuration for midterm38 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as mv
from mysite.views import HomeView, SignLogView, LoginView, RegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name = "homepage"),
    path('post/<slug:slug>/', mv.showpost, name = "showpost"),
    path('test/', mv.testme),
    path('', HomeView.as_view(), name='home'),
    path('login/', mv.login, name='login'), 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', include('midterm38.urls', namespace='midterm38')),
    path('process_returns/', process_returns, name='process_returns')]

