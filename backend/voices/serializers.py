from rest_framework import serializers
from .models import Caption, VoiceCategory, VoiceModel
from accounts.serializers import UserSerializer

class TrainCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caption
        fields = '__all__'

class TrainVoiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceCategory
        fields = ['id', 'name']

class VoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceModel
        fields = ['id', 'name']