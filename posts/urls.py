from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("create_post/", create_post, name="create_post"),
    path("all_posts/", all_posts, name="all_posts"),
    path("user_posts/<str:username>", user_posts, name="user_posts"),
    path("edit_post/", edit_post, name="edit_post"),
    path("like_post/<int:post_id>", like_post, name="like_post"),
    path("does_like_post/<int:post_id>", does_like_post, name='does_like_post'),
]
