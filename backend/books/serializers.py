from rest_framework import serializers
from .models import Fairytale, Genre, VoiceStorage, Scenario

class FairytaleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = ['id', 'title', 'image']

class FairytaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = '__all__'

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['content']


class VoiceStorageSerailizer(serializers.ModelSerializer):
    scenario = ScenarioSerializer()
    class Meta:
        model = VoiceStorage
        fields = ['scenario', 'voice_file']