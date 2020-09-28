from rest_framework import serializers
from .models import VoiceCategory
from accounts.serializers import UserSerializer

class TrainVoiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceCategory
        fields = ['id', 'name']