from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, validators=[validate_password])
    password2 = serializers.CharField(min_length=8, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'email', 'avatar', 'last_name', 'first_name', 'password', 'password2', 'created_date']

    def validate(self, attrs):
        print(attrs)
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'avatar', 'last_name', 'last_login', 'modified_date', 'created_date']
