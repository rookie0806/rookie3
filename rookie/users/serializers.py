from rest_framework import serializers
from . import models
from rookie.musics import serializers as musics_serializers
class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'profileimg',
            'username',
            'name',
        )

class UserProfileSerializer(serializers.ModelSerializer):

    lists_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'profileimg',
            'lists_count',
            'followers_count',
            'following_count',
        )


