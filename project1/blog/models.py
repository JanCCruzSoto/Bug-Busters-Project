from django.db import models

# Important
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class PostEng(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Commenteng(models.Model):
    post = models.ForeignKey(Post, related_name='commentsEng', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

#
# class PostSpa(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField()
#     intro = models.TextField()
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-date_added']
#
#
# class CommentSpa(models.Model):
#     post = models.ForeignKey(Post, related_name='commentsSpa', on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['date_added']
#
#
# class PostJap(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField()
#     intro = models.TextField()
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-date_added']
#
#
# class CommentJap(models.Model):
#     post = models.ForeignKey(Post, related_name='commentsJap', on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['date_added']



