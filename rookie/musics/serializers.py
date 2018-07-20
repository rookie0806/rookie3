from rest_framework import serializers
from . import models
from rookie.users import models as user_models

class FeedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = (
            'username',
        )

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    Song_list = MusicSerializer(many=True)
    List_creator = FeedUserSerializer() 
    class Meta:
        model = models.List
        fields = (
            'List_name',
            'Song_list',
            'List_creator',
            'created_at'
        )