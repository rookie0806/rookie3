from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListTop100(APIView):
    def get(self, request, format=None):

        List = models.Music.objects.all()
        serializer = serializers.MusicSerializer(List,many=True)

        return Response(data=serializer.data) 