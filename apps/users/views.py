import jwt
from django.conf import settings
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.models import User
from apps.users.serializers import (
    UserRegistrSerializer,
    AuthSerializer,
    UserDetailSerializer
)


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        user_payload = {
            'user_id': user.id,
            'user.email': user.email,
            'username': user.username
        }
        tokens = {
            'access_token': jwt.encode(user_payload, settings.SECRET_KEY, algorithm="HS256"),
            'refresh_token': jwt.encode(user_payload, settings.SECRET_KEY, algorithm="HS256")
        }

        response_data = {
            'user_id': user.id,
            'user.email': user.email,
            'username': user.username,
            'tokens': tokens
        }
        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class AuthView(generics.GenericAPIView):
    serializer_class = AuthSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserDetailListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, ]
