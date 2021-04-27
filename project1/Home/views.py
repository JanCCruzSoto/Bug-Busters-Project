from django.shortcuts import render, redirect

from blog.models import Post, PostEng
from blog.forms import CommentForm

# from blogEng.models import Post_e
# from blogEng.forms import CommentForm_e


def home(request):
    return render(request, "pages/home.html", {})


def about(request):
    my_context = {
        "my_text": "about us",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "pages/about.html", my_context)


def english(request):
    my_context = {
        "my_text": "english",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "pages/English.html", my_context)
    # posts = Post_e.objects.all()
    #
    # return render(request, 'pages/english.html', {'posts': posts})

def spanish(request):
    my_context = {
        "my_text": "english",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "pages/spanish.html", my_context)


def japanese(request):
    my_context = {
        "my_text": "english",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "pages/japanese.html", my_context)

def forumPage(request):

    # my_context = {
    #     "my_text": "english",
    #     "my_number": 123,
    #     "my_list": [1, 2, 3]
    #
    # }


    posts = Post.objects.all()

    return render(request, 'pages/forumPage.html', {'posts': posts})

    # return render(request, "pages/forumPage.html", my_context, {'posts': posts})




def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'pages/post_detail.html', {'post': post, 'form': form})




def contact(request):
    return render(request, "pages/contact.html", {})



