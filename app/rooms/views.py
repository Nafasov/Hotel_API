from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.blog.permission import IsAuthorOrReadOnly
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
    serializer_class = RoomsImagesSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        room_id = self.kwargs.get('room_id')
        if room_id:
            qs = qs.filter(room_id=room_id)
            return qs
        return qs.none()


class RoomContentAPIView(generics.ListAPIView):
    # room/{room_id}/content
    queryset = RoomContent.objects.all()
    serializer_class = RoomContentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        room_id = self.kwargs.get('room_id')
        if room_id:
            qs = qs.filter(room_id=room_id)
            return qs
        return qs.none()


class CommentDeleteAPIView(generics.DestroyAPIView):
    # room/{room_id}/comment/{pk}/delete
    queryset = RoomComments.objects.all()
    serializer_class = RoomCommentsSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        room_id = self.kwargs.get('room_id')
        if room_id:
            qs = qs.filter(room_id=room_id)
            return qs
        return qs.none()


class CommentAPIView(generics.ListCreateAPIView):
    # room/{room_id}/comment
    queryset = RoomComments.objects.all()
    serializer_class = RoomCommentsSerializer
    serializer_post_class = RoomCommentsPOSTSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_post_class
        return self.serializer_class

    def get_queryset(self):
        qs = super().get_queryset()
        room_id = self.kwargs.get('room_id')
        if room_id:
            qs = qs.filter(room_id=room_id)
            return qs
        return qs.none()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        room_id = self.kwargs.get('room_id')
        ctx['room_id'] = room_id
        return ctx


class RoomLikesAPIView(generics.GenericAPIView):
    queryset = RoomCommentLikes.objects.all()
    serializer_class = RoomLikesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        room_id = self.kwargs.get('room_id')
        author_id = request.user.id
        has_like = RoomCommentLikes.objects.filter(rooms_id=room_id, author_id=author_id)
        if has_like:
            has_like.delete()
            return Response({'success': True, 'message': 'Episode like remove'})
        else:
            RoomCommentLikes.objects.create(rooms_id=room_id, author_id=author_id)
            return Response({'success': True, 'message': 'Episode like add'})





