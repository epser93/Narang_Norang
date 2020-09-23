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


class FavoriteAPI(APIView):
    def get(self, request, format=None):
        fairytales = request.user.favorite.all()
        serializer = FairytaleListSerializer(fairytales, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        fairytale = Fairytale.objects.get(pk=pk)
        if fairytale.like_user.filter(pk=request.user.pk).exists():
            return Response('이미 추가되어 있습니다.')
        else:
            fairytale.like_user.add(request.user)
            return Response('추가완료')

    def delete(self, request, pk):
        fairytale = Fairytale.objects.get(pk=pk)
        if fairytale.like_user.filter(pk=request.user.pk).exists():
            fairytale.like_user.remove(request.user)
            return Response('삭제완료')
        else:
            return Response('이미 삭제되어 있습니다.')