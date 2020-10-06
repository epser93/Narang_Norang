from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Subscribe
import datetime
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()
    def get_is_subscribed(self, obj):
        subscribe = Subscribe.objects.filter(user=obj).filter(end_date__gte=datetime.datetime.today())
        if subscribe:
            return True
        return False
    class Meta:
        model = User
        fields = ['id', 'username', 'balance','first_name', 'is_staff', 'is_subscribed']

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'start_date', 'end_date', 'tid', 'is_return']
