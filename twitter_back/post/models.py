from django.db import models

from user.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="post_img/")
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")

