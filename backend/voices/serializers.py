from rest_framework import serializers
from .models import Caption, VoiceCategory, VoiceModel, TrainVoice
from accounts.serializers import UserSerializer

class TrainCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caption
        fields = '__all__'

class TrainVoiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceCategory
        fields = ['id', 'name', 'is_train']

class TrainVoiceSerializer(serializers.ModelSerializer):
    caption = TrainCaptionSerializer()
    class Meta:
        model = TrainVoice
        fields= ['id', 'train_file', 'caption']

class VoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceModel
        fields = ['id', 'name']