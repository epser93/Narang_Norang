from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrainCaptionSerializer, TrainVoiceCategorySerializer 

from .models import VoiceModel, VoiceCategory, Caption, TrainVoice, OverwriteStorage

fs = OverwriteStorage()

class TrainAPI(APIView):

    def post(self, request, category_id, caption_id):
        category = VoiceCategory.objects.get(pk=category_id, user=request.user)
        caption = Caption.objects.get(pk=caption_id)

        voice_file = request.FILES['file']
        extention = voice_file.name.split('.')[-1]
        if extention not in ['mp3', 'wav']:
            return Response('잘못된 확장자입니다.', status=status.HTTP_400_BAD_REQUEST)
        file_name = '{}_{}_{}.{}'.format(request.user.username, category_id, caption_id, extention)
        filename = fs.save(file_name, voice_file)

        train_voice = TrainVoice()
        train_voice.create(filename, category, caption, request.user)
        return Response('저장완료')

        
    def delete(self, request, category_id, caption_id):
        category = VoiceCategory.objects.get(pk=category_id, user=request.user)
        caption = Caption.objects.get(pk=caption_id)
        train_voice = TrainVoice.objects.get(user=request.user, voice_category=category, caption=caption)
        train_voice.delete()
        return Response('삭제완료')

# Create your views here.

class TrainCaption(APIView):
    def get(self, request):
        caption = Caption.objects.all()
        serializer = TrainCaptionSerializer(caption, many=True)
        return Response(serializer.data)

class TrainVoiceCategory(APIView):
    def get(self, request):
        category = VoiceCategory.objects.filter(user = request.user)
        serializer = TrainVoiceCategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        is_exist = VoiceCategory.objects.filter(user = request.user).filter(name=request.data['name']).exists()
        if not is_exist:
            category = VoiceCategory()
            category.create(request.data, request.user)
            serializer = TrainVoiceCategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('중복된 카테고리입니다.', status=status.HTTP_400_BAD_REQUEST)

class TrainVoiceCategoryDetail(APIView):
    def delete(self, request, category_id):
        category = VoiceCategory.objects.get(pk=category_id)
        if category.user == request.user:
            category.delete()
            return Response('삭제완료', status=status.HTTP_200_OK)
        return Response('권한없음', status=status.HTTP_403_FORBIDDEN)

    def put(self, request, category_id):
        category = VoiceCategory.objects.get(pk=category_id, user=request.user)
        is_exist = VoiceCategory.objects.filter(user=request.user).filter(name=request.data['name']).exists()
        if is_exist:
            return Response('중복된 카테고리입니다.', status=status.HTTP_400_BAD_REQUEST)
        category.update(request.data, request.user)
        serializer = TrainVoiceCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
