from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QnA
from .serializers import QnAListSerializer

# Create your views here.
class QnAList(APIView):
    def get(self, request, format=None):
        queryset = QnA.objects.all()
        serializer = QnAListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QnAListSerializer(data=request.data)
        print(request.user)
        # serializer.user = request.user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)