from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'user']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

