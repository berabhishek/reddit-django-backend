from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DefaultFeatures(models.Model):
    auto_id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract=True

class Post(DefaultFeatures):
    title = models.TextField()

class Comment(DefaultFeatures):
    parent_comment = models.ForeignKey('self',null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Votes(models.Model):
    auto_id = models.AutoField(primary_key=True)
    vote_direction = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)