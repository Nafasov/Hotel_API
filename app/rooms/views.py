from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import (
    RoomServices,
    Rooms,
    Booking,
    RoomImages,
    RoomContent,
    RoomComments,
    RoomCommentLikes,
    )
from .serializers import (
    RoomServicesSerializer,
    RoomsSerializer,
    BookingSerializer,
    RoomsImagesSerializer,
    RoomContentSerializer,
    RoomCommentsSerializer,
    RoomCommentsPOSTSerializer,
    RoomLikesSerializer
    )


class RoomServicesAPIView(generics.ListAPIView):
    queryset = RoomServices.objects.all()
    serializer_class = RoomServicesSerializer


class RoomsAPIView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class BookingAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class RoomImagesAPIView(generics.ListAPIView):
    # room/{room_id}/image
    queryset = RoomImages.objects.all()
    serializer_class = RoomContentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        room_id = self.kwargs.get('room_id')
        qs = qs.filter(room_id=room_id)
        return qs


class RoomContentAPIView(generics.ListAPIView):
    # room/{room_id}/content
    queryset = RoomContent.objects.all()
    serializer_class = RoomContentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        room_id = self.kwargs.get('room_id')
        qs = qs.filter(room_id=room_id)
        return qs



