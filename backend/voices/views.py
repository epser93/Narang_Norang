from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Caption, VoiceCategory
from .serializers import TrainCaptionSerializer, TrainVoiceCategorySerializer 
from rest_framework import status
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