from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BlogPostAPIView,
    SendBlogNEWAPIView,
    TagAPIView,
    BlogNEWPostAPIView,
    ContentNEWPostAPIView,
    CommentNEWPostAPIView,
    CommentNEWDeleteAPIView,
    LikeNEWPostAPIView
    )

app_name = 'blog'

router = DefaultRouter()
router.register('post', BlogPostAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('send/blog/', SendBlogNEWAPIView.as_view()),
    path('tags/', TagAPIView.as_view()),
    path('new/list/', BlogNEWPostAPIView.as_view()),
    path('new/detail/<slug:slug>/', BlogNEWPostAPIView.as_view()),
    path('new/<int:blog_id>/content/', ContentNEWPostAPIView.as_view()),
    path('new/<int:blog_id>/comment/', CommentNEWPostAPIView.as_view()),
    path('new/<int:blog_id>delete/comment/<int:pk>/', CommentNEWDeleteAPIView.as_view()),
    path('new/<int:blog_id>/like', LikeNEWPostAPIView.as_view())
]


'''
    BlogPost
        -list
        -create
        -update
        -delete
    SendBlogNEW
        -list
        -create
    Tag
        -list
    BlogNEWPost
        -list
    ContentNewBlog
        -list
    CommentNewBlog
        -list
        -create
    BlogNewLike
        -like
        -dislike
'''