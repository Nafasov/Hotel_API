from rest_framework import serializers

from app.account.serializers import UserSerializer

from .models import (
        BlogPost,
        SendBlogNEW,
        Tag,
        BlogNEWPost,
        ContentNewBlog,
        CommentNewBlog,
        BlogNewLike
        )


class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'image', 'description', 'created_date']


class BlogPostPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'image', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author_id = request.get('author_id')
        validated_data['author_id'] = author_id
        return super().create(validated_data)


class SendBlogNEWSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendBlogNEW
        fields = ['id', 'email']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class BlogNEWPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = BlogNEWPost
        fields = ['id', 'title', 'author', 'tags', 'slug', 'image', 'created_date']


class ContentNewBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentNewBlog
        fields = ['id', 'content', 'is_quote']


class CommentNewBlogPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentNewBlog
        fields = ['id', 'parent', 'message', 'created_date']
        red_only = ['created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        blog_post_id = validated_data.pop('blog_post_id')
        author_id = request.get('author_id')
        validated_data['author_id'] = author_id
        validated_data['blog_post_id'] = blog_post_id
        return super().create(validated_data)


class CommentNewBlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentNewBlog
        fields = ['id', 'author', 'parent', 'top_level_comment_id', 'message', 'created_date']


class BlogNewLikeSerializer(serializers.Serializer):
    blog_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    class Meta:
        fields = ['id', 'blog_id', 'user_id']

