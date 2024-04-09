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
        if self.request.method == "POST":
            return self.serializer_post_class
        return self.serializer_class


class SendBlogNEWAPIView(generics.ListCreateAPIView):
    queryset = SendBlogNEW.objects.all()
    serializer_class = SendBlogNEWSerializer
    permission_classes = [IsAuthenticated]


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


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
    pagination_class = None

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        if blog_id:
            qs = qs.filter(blog_post_id=blog_id)
            return qs
        return qs.none()


class CommentNEWPostAPIView(generics.ListCreateAPIView):
    # blog/{}/comment/ --> list, create
    # blog/{}/comment/{comment_id} --> update, delete

    queryset = CommentNewBlog.objects.all()
    serializer_class = CommentNewBlogSerializer
    serializer_post_class = CommentNewBlogPOSTSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        if blog_id:
            qs = qs.filter(blog_post_id=blog_id)
            return qs
        return qs.none()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return self.serializer_post_class
        return self.serializer_class

    def get_serializer_context(self):
        context = super().get_serializer_context()
        blog_id = self.kwargs.get("blog_id")
        context["blog_post_id"] = blog_id
        return context


class CommentNEWDeleteAPIView(generics.DestroyAPIView):
    # blog/new/{blog_id}/comment/{comment_id}/
    queryset = CommentNewBlog.objects.all()
    serializer_class = CommentNewBlogSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        if blog_id:
            qs = qs.filter(blog_post_id=blog_id)
            return qs
        return qs.none()


class LikeNEWPostAPIView(generics.GenericAPIView):
    # blog/new/{blog_id}/like/
    queryset = CommentNewBlog.objects.all()
    serializer_class = BlogNewLikeSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = None

    def post(self, request, *args, **kwargs):
        blog_id = self.kwargs.get("blog_id")
        author_id = request.user.id
        has_like = BlogNewLike.objects.filter(blog_post_id=blog_id, author_id=author_id)
        if has_like:
            has_like.delete()
            return Response({'success': True, 'message': 'Episode like remove'})
        else:
            BlogNewLike.objects.create(blog_post_id=blog_id, author_id=author_id)
            return Response({'success': True, 'message': 'Episode like add'})
