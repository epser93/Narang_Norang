from rest_framework import serializers
from .models import Fairytale, Genre, VoiceStorage, Scenario, BookMark

class FairytaleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = ['id', 'title', 'image', 'is_pay']

class FairytaleDetailSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        user = self.context.get('user')
        if obj.like_user.filter(pk=user.id).exists():
            return True
        return False

    class Meta:
        model = Fairytale
        fields = ['id', 'title', 'summary', 'image', 'date', 'writer', 'Genre', 'is_liked']


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
        fields = ['id','scenario', 'voice_file']


class ScenarioIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id', 'content']
        
        
class BookmarkSerializer(serializers.ModelSerializer):
    fairytale = FairytaleListSerializer()
    class Meta:
        model = BookMark
        fields = ['id', 'fairytale']


class BookmarkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = ['id', 'page']
