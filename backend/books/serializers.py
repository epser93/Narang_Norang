from rest_framework import serializers
from .models import Fairytale, Genre

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