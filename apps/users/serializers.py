from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.menu.serializers import MenuSerializer


class UserTokenSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    class Meta:
        fields = (
            'access_token',
            'refresh_token',
        )


class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {password: "The passwords didn't match"})
        user.set_password(password)
        user.save()
        return user


class AuthSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist.')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid password.')

        refresh = RefreshToken.for_user(user)

        return {
            'user_id': user.id,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }


class UserDetailSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'menus', ]
