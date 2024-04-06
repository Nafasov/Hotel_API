from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import (
    UserRegistrationSerializer,
    UserSerializer
    )


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class MyProfileAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)