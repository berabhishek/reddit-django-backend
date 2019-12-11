from rest_framework import serializers
from posts.models import Post, Comment, Comment_Reply, Nested_Reply

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude =[]

class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_Reply
        exclude = []

class NestedReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nested_Reply
        exclude = []