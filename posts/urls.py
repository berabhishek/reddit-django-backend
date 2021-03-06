from django.urls import path, re_path
from . import views
from rest_framework.authtoken import views as authview
urlpatterns = [
    path('posts', views.Post_View.as_view(), name="all_posts"),
    path('post/<int:id>', views.Post_View.as_view(), name="all_posts"),
    re_path(r'comments/(?P<id>[\d/]+)$', views.Comment_View.as_view(), name="all_comments"),
    path('add_comment', views.Comment_View.as_view(), name="add_comments"),
    path('usertoken', authview.obtain_auth_token, name="user_token"),
    path('create_user', views.create_user, name="create_user"),
    path('check_user', views.check_user, name="check_user"),
    path('vote_post', views.VotePost.as_view(), name="vote_post"),
    path('vote_comment', views.VoteComment.as_view(), name="vote_comment")
]