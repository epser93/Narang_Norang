from .models import Fairytale, Genre, VoiceStorage, BookMark, Scenario
from voices.models import VoiceModel, OverwriteStorage
from accounts.models import Subscribe
from .serializers import (FairytaleListSerializer, FairytaleDetailSerializer, 
GenreListSerializer, VoiceStorageSerailizer, ScenarioIdSerializer, BookmarkSerializer, BookmarkDetailSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime


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
        fairytale = Fairytale.objects.get(pk=pk)
        if fairytale.is_pay == True:
            subscribe = Subscribe.objects.filter(user=request.user).filter(end_date__gte=datetime.datetime.today())
            if not subscribe:
                return Response("이용권이 없습니다. 결제 후 사용해 주세요!", status=status.HTTP_403_FORBIDDEN)
        voice_model = VoiceModel.objects.get(pk=model_pk)
        voice_storage = VoiceStorage.objects.filter(fairytale=fairytale).filter(voice_model=voice_model)
        caption = Scenario.objects.filter(fairytale=fairytale)
        if len(voice_storage) != len(caption):
            return Response("음성 데이터가 생성되지 않았습니다. 관리자에게 문의해주세요", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = VoiceStorageSerailizer(voice_storage, many=True)
        return Response(serializer.data)


# 삭제예정
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

# 삭제예정
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
        fairytale = Fairytale.objects.get(pk=pk)
        bookmark = BookMark.objects.filter(fairytale=fairytale).filter(user=request.user)
        if not bookmark:
            bookmark = BookMark()
            bookmark.create(request.data, request.user, fairytale)
        else:
            bookmark = bookmark[0]
            bookmark.update(request.data, request.user, fairytale)
        return Response('북마크 등록 완료')

    def get(self, request, pk):
        bookmark = BookMark.objects.filter(fairytale=pk).filter(user=request.user)
        serializer = BookmarkDetailSerializer(bookmark, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        bookmark = BookMark.objects.filter(fairytale=pk).filter(user=request.user)
        bookmark.delete()
        return Response("삭제완료")


class FairytailSearch(APIView):
    def get(self, request, fairytale_name):
        fairytales = Fairytale.objects.filter(title__icontains=fairytale_name)
        serializer = FairytaleListSerializer(fairytales, many=True)
        return Response(serializer.data)
