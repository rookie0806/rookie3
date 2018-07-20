from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rookie.users import models as user_models
# Create your views here.

class ListTop100(APIView):
    def get(self, request, format=None):

        List = models.Music.objects.all()
        serializer = serializers.MusicSerializer(List,many=True)

        return Response(data=serializer.data) 

class ListView(APIView):
    def get(slef, request, format=None):

        List = models.List.objects.all()
        serializer = serializers.ListSerializer(List,many=True)

        return Response(data=serializer.data)

class Feed(APIView):

    def get(self, request, format=None):   
        user = request.user
        following_users = user.following.all()
        play_lists = [] 
        for following_user in following_users:
            song_lists = following_user.lists.all()[:3]
            for song_list in song_lists:
                play_lists.append(song_list)

        sorted_list = sorted(play_lists,key=get_key)
        serializer = serializers.ListSerializer(sorted_list,many=True)

        return Response(serializer.data)

def get_key(List):
    return List.created_at