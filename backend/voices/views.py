from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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