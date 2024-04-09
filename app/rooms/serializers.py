from rest_framework import serializers

from app.account.serializers import UserSerializer
from .models import (
    RoomServices,
    Rooms,
    Booking,
    RoomImages,
    RoomContent,
    RoomComments,
    RoomCommentLikes,
    )


class RoomServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomServices
        fields = ['id', 'title', 'image', 'created_date']


class RoomsSerializer(serializers.ModelSerializer):
    services = RoomServicesSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Rooms
        fields = ['id', 'title', 'author', 'services', 'bed', 'cost', 'size', 'adults', 'children', 'capacity', 'created_date']


class RoomsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = ['id', 'image']


class RoomContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomContent
        fields = ['id', 'content', 'is_check']


class RoomCommentsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = RoomComments
        fields = ['id', 'author', 'comment', 'created_date']


class RoomCommentsPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomComments
        fields = ['id', 'comment', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author_id = request.user.id
        room_id = self.context.get('room_id')
        validated_data['author_id'] = author_id
        validated_data['room_id'] = room_id
        return super().create(validated_data)


class RoomLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCommentLikes
        fields = ['id']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'room', 'author', 'check_out', 'check_out', 'adults', 'children']