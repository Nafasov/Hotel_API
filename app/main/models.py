from django.db import models

from app.blog.models import BaseModel


class AboutUs(BaseModel):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='about/')
    content = models.TextField()

    def __str__(self):
        return self.title


class MeContact(BaseModel):
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=35, null=True, blank=True)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)


class Service(BaseModel):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='service/')


class Partners(BaseModel):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='partners/')
    url = models.URLField(null=True, blank=True)


class HomeBanner(BaseModel):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='banner/')
    description = models.TextField()