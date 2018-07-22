from rest_framework import serializers
from . import models

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'profileimg',
            'username',
            'name',
        )

class UserProfileSerializer(serializers.ModelSerializer):

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

