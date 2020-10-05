from .models import Fairytale, Genre, VoiceStorage, Scenario
from .serializers import FairytaleListSerializer, FairytaleDetailSerializer, GenreListSerializer, VoiceStorageSerailizer, ScenarioIdSerializer
from voices.models import VoiceModel, OverwriteStorage
from .models import Fairytale, Genre, VoiceStorage, BookMark
from .serializers import (FairytaleListSerializer, FairytaleDetailSerializer, 
GenreListSerializer, VoiceStorageSerailizer, BookmarkSerializer, BookmarkDetailSerializer)
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
        serializer = FairytaleDetailSerializer(fairytale, context={'user' : request.user })
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


class VoiceStoageAPI(APIView):
    def get(self, request, pk, model_pk, format=None):
        # to-do 읽을 수 있는 동화책인지 검증
        fairytale = Fairytale.objects.get(pk=pk)
        # to-do 사용가능한 목소리인지 검증 필요
        voice_model = VoiceModel.objects.get(pk=model_pk)
        voice_storage = VoiceStorage.objects.filter(fairytale=fairytale).filter(voice_model=voice_model)
        serializer = VoiceStorageSerailizer(voice_storage, many=True)
        return Response(serializer.data)


class AddScenario(APIView):

    def get(self, request, f_id):
        fairytale = Fairytale.objects.get(pk=f_id)
        scenarios = Scenario.objects.filter(fairytale=fairytale)
        serializer = ScenarioIdSerializer(scenarios, many=True)
        return Response(serializer.data)

    def post(self, request, f_id):
        fairytale = Fairytale.objects.get(pk=f_id)
        content = request.data['content']
        content = content.split('\n')
        for i in content:
            i = i.lstrip()
            if len(i) == 0:
                continue
            scenario = Scenario()
            scenario.fairytale = fairytale
            scenario.content = i
            scenario.save()
        return Response('ok')


fs = OverwriteStorage()

class AddVoiceStorage(APIView):

    def post(self, request, f_id, s_id, m_id):
        fairytale = Fairytale.objects.get(pk=f_id)
        scenario = Scenario.objects.get(pk=s_id)
        model = VoiceModel.objects.get(pk=m_id)

        voice_file = request.FILES['file']
        extention = voice_file.name.split('.')[-1]
        file_name = '{}_{}_{}.{}'.format(fairytale.title, m_id, s_id, extention)
        filename = fs.save(file_name, voice_file)
        
        voice_storage = VoiceStorage()
        voice_storage.fairytale = fairytale
        voice_storage.scenario = scenario
        voice_storage.voice_file = filename
        voice_storage.voice_model = model
        voice_storage.save()

        return Response('ok')
class BookMarkAPI(APIView):
    def get(self, request):
        bookmarks = BookMark.objects.filter(user=request.user)
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)


class BookmarkDetailAPI(APIView):
    def post(self, request, pk):
        bookmark = BookMark.objects.filter(fairytale=pk)
        fairytale = Fairytale.objects.get(pk=pk)
        if not bookmark:
            bookmark = BookMark()
            bookmark.create(request.data, request.user, fairytale)
        else:
            bookmark = bookmark[0]
            bookmark.update(request.data, request.user, fairytale)
        return Response('북마크 등록 완료')

    def get(self, request, pk):
        bookmark = BookMark.objects.filter(fairytale=pk)
        serializer = BookmarkDetailSerializer(bookmark, many=True)
        return Response(serializer.data)
