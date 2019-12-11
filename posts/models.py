from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DefaultFeatures(models.Model):
    auto_id = models.AutoField(primary_key=True)
    likes = models.IntegerField(name="Likes")
    text = models.TextField(name="Content")
    date = models.DateTimeField(name="Posted Date", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + str(self.post_text[:20])+"..."
    
    def created_within_hours(self, hrs):
        return True
    
    def comment_count(self):
        return 0
    class Meta:
        abstract = True

class Post(DefaultFeatures):
    pass

class Comment(DefaultFeatures):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment_Reply(DefaultFeatures):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Nested_Reply(DefaultFeatures):
    reply = models.ForeignKey("self", on_delete=models.CASCADE)