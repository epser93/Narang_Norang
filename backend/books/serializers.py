from rest_framework import serializers
from .models import Fairytale

class FairytaleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairytale
        fields = ['id', 'title', 'image']

