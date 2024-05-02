from colors.models import Color, Palette
from rest_framework import serializers
from users.models import User


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name')


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name')


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ('id', 'name')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'palette_id', 'name', 'hex')
        read_only_fields = ('name', 'id')
