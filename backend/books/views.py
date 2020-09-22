from .models import Fairytale, Genre
from .serializers import FairytaleListSerializer, FairytaleDetailSerializer, GenreListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class FairytaleList(APIView):
    def get(self, request, format=None):
        queryset = Fairytale.objects.all()
        serializer = FairytaleListSerializer(queryset, many=True)
        return Response(serializer.data)

class FairytaleDetail(APIView):
    def get(self, request, pk):
        fairytale = Fairytale.objects.get(pk=pk)
        serializer = FairytaleDetailSerializer(fairytale)
        return Response(serializer.data)

class GenreList(APIView):
    def get(self, request, format=None):
        queryset = Genre.objects.all()
        serializer = GenreListSerializer(queryset, many=True)
        return Response(serializer.data)