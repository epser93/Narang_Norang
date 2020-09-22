from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QnA
from .serializers import QnAListSerializer


# Create your views here.
class QnAList(APIView):
    def get(self, request, format=None):
        if request.user.is_staff:
            qnas = QnA.objects.filter(is_answer=False)
        else:
            qnas = QnA.objects.filter(user=request.user)
        serializer = QnAListSerializer(qnas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qna = QnA()
        qna.create(request.data, request.user)
        serializer = QnAListSerializer(qna)
        return Response(serializer.data)


class QnADetail(APIView):
    def get(self, request, pk):
        qna = QnA.objects.get(pk=pk, user=request.user)
        serializer = QnAListSerializer(qna)
        return Response(serializer.data)

    def put(self, request, pk):
        qna = QnA.objects.get(pk=pk, user=request.user)
        qna.update(request.data)
        serializer = QnAListSerializer(qna)
        return Response(serializer.data)

    def delete(self, request, pk):
        qna = QnA.objects.get(pk=pk)
        if request.user.is_staff or request.user == qna.user:
            qna.delete()
            return Response("삭제완료", status=status.HTTP_200_OK)
        return Response("권한없음", status=status.HTTP_403_FORBIDDEN)