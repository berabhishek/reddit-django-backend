from django.urls import path
from . import views
from rest_framework.authtoken import views as authview
urlpatterns = [
    path('view', views.Post_View.as_view(), name="all_posts"),
    path('comments/<str:id>', views.all_comments, name="all_comments"),
    path('usertoken', authview.obtain_auth_token, name="user_token")
]