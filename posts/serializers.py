from rest_framework import serializers
from posts.models import Post, Comment, Votes

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude =[]