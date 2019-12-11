from rest_framework import serializers
from posts.models import Post, Comment, Comment_Reply, Nested_Reply

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = ['auto_id', 'likes', 'text', 'date', 'user', 'post']

class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment_Reply
        fields = ['auto_id', 'likes', 'text', 'date', 'user', 'comment']

class NestedReplySerializer(serializers.ModelSerializer):
    class Meta:
        models = Nested_Reply
        fields = ['auto_id', 'likes', 'text', 'date', 'user', 'reply']