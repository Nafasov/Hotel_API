from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BlogPostAPIView,
    SendBlogNEWAPIView,
    TagAPIView,
    BlogNEWPostAPIView,
    ContentNEWPostAPIView,
    CommentNEWPostAPIView,
    LikeNEWPostAPIView
    )

app_name = 'blog'

router = DefaultRouter()
router.register('blog', BlogPostAPIView)
router.register('comment', CommentNEWPostAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('send/blod/', SendBlogNEWAPIView.as_view()),
    path('tags/', TagAPIView.as_view()),
    path('list/', BlogNEWPostAPIView.as_view()),
    path('detail/<slug:slug>/', BlogNEWPostAPIView.as_view()),
    path('<int:blog_id>/content/', ContentNEWPostAPIView.as_view()),
    path('<int:blog_id>/', include(router.urls)),
    path('<int:blog_id>/like', LikeNEWPostAPIView.as_view())
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