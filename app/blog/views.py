from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permission import IsAuthorOrReadOnly

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


class BlogPostAPIView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    serializer_post_class = BlogPostPOSTSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.serializer_class
        return self.serializer_post_class


class SendBlogNEWAPIView(generics.ListCreateAPIView):
    queryset = SendBlogNEW.objects.all()
    serializer_class = SendBlogNEWSerializer
    permission_classes = [IsAuthenticated]


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogNEWPostAPIView(generics.ListAPIView):
    # blog/detail/{slug}/ --> detail
    queryset = BlogNEWPost.objects.all()
    serializer_class = BlogNEWPostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.kwargs.get("slug")
        if slug:
            qs = qs.filter(slug=slug)
            return qs
        return qs


class ContentNEWPostAPIView(generics.ListAPIView):
    # blog/{blog_id}/content/
    queryset = ContentNewBlog.objects.all()
    serializer_class = ContentNewBlogSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        qs = qs.filter(blog_id=blog_id)
        return qs


class CommentNEWPostAPIView(viewsets.ModelViewSet):
    # blog/{}/comment/ --> list, create
    # blog/{}/comment/{comment_id} --> update, delete

    queryset = CommentNewBlog.objects.all()
    serializer_class = CommentNewBlogSerializer
    serializer_post_class = CommentNewBlogPOSTSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        qs = qs.filter(blog_id=blog_id)
        return qs

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.serializer_class
        return self.serializer_post_class

    def get_serializer_context(self):
        context = super().get_serializer_context()
        blog_id = self.kwargs.get("blog_id")
        context["blog_id"] = blog_id
        return context


class LikeNEWPostAPIView(generics.GenericAPIView):
    queryset = CommentNewBlog.objects.all()
    serializer_class = BlogNewLikeSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def post(self, request, *args, **kwargs):
        blog_id = self.kwargs.get("blog_id")
        user_id = request.user.id
        has_like = BlogNewLike.objects.filter(blog_id=blog_id, user_id=user_id).exists()
        if has_like:
            has_like.delete()
            return Response({'success': True, 'message': 'Episode like remove'})
        else:
            BlogNewLike.objects.create(blog_id=blog_id, user_id=user_id)
            return Response({'success': True, 'message': 'Episode like add'})
