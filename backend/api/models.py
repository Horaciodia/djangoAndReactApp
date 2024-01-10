from django.db import models
from django.core.validators import MinLengthValidator

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, related_name='post_comments', blank=True)

class UserModel(models.Model):
    username = models.CharField(max_length=25, unique=True, validators=[MinLengthValidator(limit_value=5)])
    password = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(limit_value=5)])
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post, related_name='user_posts', blank=True)