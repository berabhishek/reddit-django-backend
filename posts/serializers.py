from rest_framework import serializers
from posts.models import Post, Comment, Votes_Post, Votes_Comment
from rest_framework.fields import CurrentUserDefault

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []
    likes = serializers.IntegerField(read_only=True)
    dislikes = serializers.IntegerField(read_only=True)
    user_vote = serializers.SerializerMethodField()

    def get_user_vote(self, obj):
        try:
            user = self.context["request"].user
            if user is None:
                return 0
            vote = Votes_Post.objects.get(user=user.id, post_id=obj)
            return vote.vote_direction
        except:
            return 0

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude =[]

class VotePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes_Post
        exclude = []

class VoteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes_Comment
        exclude = []