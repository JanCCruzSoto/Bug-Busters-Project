from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import profiles
from .forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def profile_create_view(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, "profiles/profile_create.html", context)


def signup(request):
    if request.method == 'POST':
        User_form = UserCreationForm(request.POST)
        Profile_form = ProfileForm(request.POST)
        if User_form.is_valid() and Profile_form.is_valid():
            user = User_form.save()
            auth_login(request, user)
            user.save()
            profile = Profile_form.save()
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        User_form = UserCreationForm()
        Profile_form = ProfileForm()
    return render(request, 'pages/signup.html', {'user_form': User_form, 'profile_form': Profile_form})


def profile_detail_view(request):
    obj = profiles.objects.get(id=1)
    # context = {
    #   'email': obj.email,
    #   'name': obj.name
    # }
    context = {
        'object': obj
    }
    return render(request, "profiles/detail.html", context)
