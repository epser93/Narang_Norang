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
        fields = ['id', 'name']

class TrainVoiceSerializer(serializers.ModelSerializer):
    voice_category = TrainVoiceCategorySerializer()
    caption = TrainCaptionSerializer()
    class Meta:
        model = TrainVoice
        fields= ['id', 'voice_category', 'train_file', 'caption']

class VoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceModel
        fields = ['id', 'name']