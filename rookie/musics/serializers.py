from rest_framework import serializers
from . import models
class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Music
        fields = '__all__'
        ordering = ('Grade',)