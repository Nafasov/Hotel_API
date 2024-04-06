from django.contrib import admin


from .models import (
    BlogPost,
    SendBlogNEW,
    Tag,
    BlogNEWPost,
    ContentNewBlog,
    CommentNewBlog,
    BlogNewLike,
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", 'author', 'title', 'created_date', )
    list_filter = ("created_date", )
    search_fields = ('title', 'author', )
    readonly_fields = ('created_date', 'modified_date', )
    date_hierarchy = 'created_date'
    list_per_page = 10


@admin.register(SendBlogNEW)
class SendBlogNEWAdmin(admin.ModelAdmin):
    list_display = ("id", "email",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', )


class ContentNewBlogAdmin(admin.TabularInline):
    model = ContentNewBlog
    extra = 1


class BlogNewLikeAdmin(admin.TabularInline):
    model = BlogNewLike
    extra = 1


@admin.register(BlogNEWPost)
class BlogNEWPostAdmin(admin.ModelAdmin):
    inlines = (ContentNewBlogAdmin, BlogNewLikeAdmin)
    list_display = ("id", 'author', 'title', 'created_date', )
    list_filter = ("created_date", )
    search_fields = ('title', 'author', 'id')
    readonly_fields = ('created_date', 'modified_date', 'slug')
    filter_horizontal = ('tags', )
    date_hierarchy = 'created_date'
    ordering = ('id', )
    list_per_page = 10


@admin.register(CommentNewBlog)
class CommentNewBlogAdmin(admin.ModelAdmin):
    list_display = ("id",'created_date', )
    list_filter = ("created_date", )
    search_fields = ('title', 'author', )
    date_hierarchy = 'created_date'
    list_per_page = 15