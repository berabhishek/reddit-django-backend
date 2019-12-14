from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer, VotePostSerializer, VoteCommentSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
            serializer = PostSerializer(post, many=True, context={'request': request})
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                post = Post.objects.get(auto_id=id)
                serializer = PostSerializer(post, many=False, context={'request': request})
                return JsonResponse(serializer.data, safe=False)
            except:
                return JsonResponse([], safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = PostSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Comment_View(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id, format=None):
        try :
            ids = [int(i) for i in id.split("/")]
            comments = Comment.objects.filter(post=Post.objects.get(auto_id=ids[0]))
            if len(ids) == 2:
                comments = comments.filter(parent_comment = id[2])
            serializer = CommentSerializer(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse(["err"], safe=False)
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data["username"]
        password = data["password"]
        try:
            existing_user = User.objects.get(username=username)
            return JsonResponse({"status": "User exists"}, status=201)
        except:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return JsonResponse({"status": "success"}, status=201)

@csrf_exempt
def check_user(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data["username"]
        password = data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({"status": "success"}, status=201)
        return JsonResponse({"status": "failure"}, status=201)

class VotePost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = VotePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class VoteComment(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data["user"] = request.user.id
        serializer = VoteCommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)