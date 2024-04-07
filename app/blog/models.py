from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from app.account.models import User


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/post', null=True, blank=True)
    description = models.TextField()


class SendBlogNEW(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BlogNEWPost(BaseModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog/new')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class ContentNewBlog(BaseModel):
    blog_post = models.ForeignKey(BlogNEWPost, on_delete=models.CASCADE, related_name='contents', null=True)
    content = models.TextField()
    is_quote = models.BooleanField(default=False)


class CommentNewBlog(BaseModel):
    blog_post = models.ForeignKey(BlogNEWPost, on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    message = models.TextField()

    @property
    def blog_children(self):
        if not self.parent:
            return CommentNewBlog.objects.filter(top_level_comment_id=self.id)
        return None


class BlogNewLike(BaseModel):
    blog_post = models.ForeignKey(BlogNEWPost, on_delete=models.CASCADE, related_name='likes', null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


@receiver(pre_save, sender=CommentNewBlog)
def comment_pre_save(sender, instance, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


@receiver(pre_save, sender=BlogNEWPost)
def blog_post_pre_save(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + ' - ' + str(timezone.now().date()))
