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
    
    @property
    def likes(self):
        return len(Votes_Post.objects.filter(post_id=self.auto_id).filter(vote_direction=1))
    
    @property
    def dislikes(self):
        return len(Votes_Post.objects.filter(post_id=self.auto_id).filter(vote_direction=-1))

class Comment(DefaultFeatures):
    parent_comment = models.ForeignKey('self',null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Votes_Parent(models.Model):
    class Meta:
        abstract = True
    auto_id = models.AutoField(primary_key=True)
    vote_direction = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Votes_Post(Votes_Parent):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Votes_Comment(Votes_Parent):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
