from rest_framework import serializers
from posts.models import Post, Comment, Votes_Post, Votes_Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []
    likes = serializers.IntegerField(read_only=True)
    dislikes = serializers.IntegerField(read_only=True)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude =[]