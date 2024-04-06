from django.db import models
from app.account.models import User
from app.blog.models import BaseModel


class RoomServices(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Rooms(BaseModel):
    title = models.CharField(max_length=221)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(RoomServices, related_name='services')
    bed = models.CharField(max_length=221)
    cost = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True)
    capacity = models.CharField(max_length=40)

    def __str__(self):
        return self.bed


class RoomContent(models.Model):
    content = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='contents')
    is_check = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class RoomImages(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')


class Booking(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='datas')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.check_in} - {self.check_out}'


class RoomComments(BaseModel):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()


class RoomCommentLikes(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='rooms', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
