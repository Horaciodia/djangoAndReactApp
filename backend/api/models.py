from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    postId = models.TextField(default='null')
    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, related_name='post_comments', blank=True)