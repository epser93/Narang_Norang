from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import QnA, FaQ, FaQCategory, QnaReply


class QnAReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = QnaReply
        fields = ['id', 'content', 'create_date']


class QnASerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    qna_reply = QnAReplySerializer(many=True)
    class Meta:
        model = QnA
        fields =['id', 'title', 'content', 'create_date', 'is_answer', 'user', 'qna_reply']


class FaQCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FaQCategory
        fields = ['id', 'name']


class FaQSerializer(serializers.ModelSerializer):
    faq_category = FaQCategorySerializer()
    class Meta:
        model = FaQ
        fields = ['id','title','content','faq_category']