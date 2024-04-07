from django.urls import path

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


urlpatterns = [

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