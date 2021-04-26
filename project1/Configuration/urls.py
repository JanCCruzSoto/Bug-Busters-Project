"""Configuration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Home import views
from profiles import views as pviews
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from Home.views import english, spanish, japanese, post_detail, forumPage
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup/', pviews.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('create/', pviews.profile_create_view),
    path('japanese/', japanese),
    path('english/', english),
    path('spanish/', spanish),

    path('forumPage/', forumPage),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),

    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('profile/<int:pk>', pviews.profile_detail_view, name='profile')
    #  path('', home_view, name='home')

]
