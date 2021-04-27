from django.contrib import admin

# Register your models here.
from .models import Post, PostEng

admin.site.register(Post)

admin.site.register(PostEng)