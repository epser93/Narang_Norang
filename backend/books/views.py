from .models import Fairytale
from .serializers import FairytaleListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class FairytaleList(APIView):
    def get(self, request, format=None):
        queryset = Fairytale.objects.all()
        serializer = FairytaleListSerializer(queryset, many=True)
        return Response(serializer.data)

