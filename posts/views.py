from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.
class Post_View(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def all_posts(request):
    """
    List all posts or create new post.
    """
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def all_comments(request, id):
    try :
        comments = Comment.objects.get(auto_id=id)
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse([], safe=False)