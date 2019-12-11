from django.urls import path
from . import views
from rest_framework.authtoken import views as authview
urlpatterns = [
    path('posts', views.Post_View.as_view(), name="all_posts"),
    path('post/<int:id>', views.Post_View.as_view(), name="all_posts"),
    path('comments/<int:id>', views.Comment_View.as_view(), name="all_comments"),
    path('add_comments', views.Comment_View.as_view(), name="add_comments"),
    path('comment_replies/<int:id>', views.Comment_Reply_View.as_view(), name="all_comment_replies"),
    path('add_comment_replies', views.Comment_Reply_View.as_view(), name="add_comment_replies"),
    path('nested_replies/<int:id>', views.Nested_Reply_View.as_view(), name="all_nested_replies"),
    path('add_nested_replies', views.Nested_Reply_View.as_view(), name="add_nested_replies"),
    path('usertoken', authview.obtain_auth_token, name="user_token")
]