from django.db import models

from app.blog.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
