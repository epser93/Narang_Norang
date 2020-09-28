from rest_framework import serializers
from .models import Caption, VoiceCategory
from accounts.serializers import UserSerializer

class TrainCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caption
        fields = '__all__'

class TrainVoiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceCategory
        fields = ['id', 'name']