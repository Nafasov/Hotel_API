from django.urls import path

from .views import (
    RoomServicesAPIView,
    RoomsAPIView,
    BookingAPIView,
    RoomImagesAPIView,
    RoomContentAPIView,
    CommentAPIView,
    CommentDeleteAPIView,
    RoomLikesAPIView
    )

app_name = 'rooms'

urlpatterns = [
    path('services/', RoomServicesAPIView.as_view()),
    path('room/', RoomsAPIView.as_view()),
    path('<int:room_id>/images/', RoomImagesAPIView.as_view()),
    path('<int:room_id>/content/', RoomContentAPIView.as_view()),
    path('<int:room_id>/comments/', CommentAPIView.as_view()),
    path('<int:room_id>/comments/<int:comment_id>/', CommentDeleteAPIView.as_view()),
    path('<int:room_id>/booking/', BookingAPIView.as_view()),
    path('<int:room_id>/like/', RoomLikesAPIView.as_view()),
]


'''
    RoomServices
        -list
    Rooms
        -list
    Booking
        -booking
    RoomImages
        -list
    RoomContent
        -list
    RoomComments
        -list
        -create
        -delete
    RoomCommentLikes
        -like
'''