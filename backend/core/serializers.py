from rest_framework import serializers
from .models import TokenT


class TokenTSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenT
        fields = '__all__'

class TokenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenT
        fields = ('media_url', 'owner')
