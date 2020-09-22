from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import QnA

class QnAListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = QnA
        fields =['id', 'title', 'content', 'create_date', 'is_answer', 'user']