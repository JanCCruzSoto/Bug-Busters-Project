from django.shortcuts import render
from django.http import HttpResponse
from .models import Forum


# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home Page</h1>")


def forum_view(request):
    forums = Forum.objects.all()

    return render(request, 'pages/forum.html', {'forums': forums})
