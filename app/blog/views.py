from rest_framework import viewsets, generics


from .serializers import (
        BlogPostSerializer,
        BlogPostPOSTSerializer,
        SendBlogNEWSerializer,
        TagSerializer,
        BlogNEWPostSerializer,
        ContentNewBlogSerializer,
        CommentNewBlogPOSTSerializer,
        CommentNewBlogSerializer,
        BlogNewLikeSerializer,
        )

from .models import (
        BlogPost,
        SendBlogNEW,
        Tag,
        BlogNEWPost,
        ContentNewBlog,
        CommentNewBlog,
        BlogNewLike
        )

