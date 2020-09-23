from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QnA, FaQ
from .serializers import QnASerializer, FaQSerializer


# Create your views here.
class QnAList(APIView):
    def get(self, request, format=None):
        if request.user.is_staff:
            qnas = QnA.objects.filter(is_answer=False)
        else:
            qnas = QnA.objects.filter(user=request.user)
        serializer = QnASerializer(qnas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qna = QnA()
        qna.create(request.data, request.user)
        serializer = QnASerializer(qna)
        return Response(serializer.data)


class QnADetail(APIView):
    def get(self, request, pk):
        qna = QnA.objects.get(pk=pk, user=request.user)
        serializer = QnASerializer(qna)
        return Response(serializer.data)

    def put(self, request, pk):
        qna = QnA.objects.get(pk=pk, user=request.user)
        qna.update(request.data)
        serializer = QnASerializer(qna)
        return Response(serializer.data)

    def delete(self, request, pk):
        qna = QnA.objects.get(pk=pk)
        if request.user.is_staff or request.user == qna.user:
            qna.delete()
            return Response("삭제완료", status=status.HTTP_200_OK)
        return Response("권한없음", status=status.HTTP_403_FORBIDDEN)

class FaQList(APIView):
    def get(self, request):
        faq = FaQ.objects.all()
        serializer = FaQSerializer(faq, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if request.user.is_staff:
            faq = FaQ()
            faq.create(request.data)
            serializer = FaQSerializer(faq)
            return Response(serializer.data)
        return Response('권한 없음', status=status.HTTP_403_FORBIDDEN)
    

class FaQDetail(APIView):
    def get(self, request, pk):
        faq = FaQ.objects.get(pk=pk)
        serializer = FaQSerializer(faq)
        return Response(serializer.data)

    def put(self, request, pk):
        if request.user.is_staff:
            faq = FaQ.objects.get(pk=pk)
            faq.update(request.data)
            serializer = FaQSerializer(faq)
            return Response(serializer.data)
        return Response('권한 없음', status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        if request.user.is_staff:
            faq = FaQ.objects.get(pk=pk)
            faq.delete()
            return Response("삭제완료", status=status.HTTP_200_OK)
        return Response("권한없음", status=status.HTTP_403_FORBIDDEN)