from rest_framework import serializers
from .models import QnA

class QnAListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        depth = 1
        fields ='__all__'

