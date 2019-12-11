from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from posts.models import Post, Comment, Comment_Reply, Nested_Reply
from posts.serializers import PostSerializer, CommentSerializer, CommentReplySerializer, NestedReplySerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.
class Post_View(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id=None, format=None):
        if id is None:
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                post = Post.objects.get(auto_id=id)
                serializer = PostSerializer(post, many=False)
                return JsonResponse(serializer.data, safe=False)
            except:
                return JsonResponse([], safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Comment_View(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id, format=None):
        try :
            comments = Comment.objects.filter(post = Post.objects.get(auto_id=id))
            serializer = CommentSerializer(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse([Post.objects.get(auto_id=id)], safe=False)
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Comment_Reply_View(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id, format=None):
        try :
            comment_replies = Comment_Reply.objects.filter(comment = Comment.objects.get(auto_id=id))
            serializer = CommentReplySerializer(comment_replies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse([], safe=False)
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = CommentReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Nested_Reply_View(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id, format=None):
        try :
            nested_replies = Nested_Reply.objects.filter(reply = Comment_Reply.objects.get(auto_id=id))
            serializer = NestedReplySerializer(nested_replies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse([], safe=False)
    
    def post(self, request, id, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = NestedReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#Views to populate entire view
