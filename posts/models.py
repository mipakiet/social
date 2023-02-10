from datetime import datetime
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    pub_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_like')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return Comment.objects.filter(post__id=self.id).count()


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    pub_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
