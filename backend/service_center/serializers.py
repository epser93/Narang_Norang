from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import QnA, FaQ, FaQCategory

class QnASerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = QnA
        fields =['id', 'title', 'content', 'create_date', 'is_answer', 'user']

class FaQCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FaQCategory
        fields = ['id', 'name']

class FaQSerializer(serializers.ModelSerializer):
    faq_category = FaQCategorySerializer()
    class Meta:
        model = FaQ
        fields = ['id','title','content','faq_category']