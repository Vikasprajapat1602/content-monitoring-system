from rest_framework import serializers
from .models import Keyword, Flag

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name']

    def validate_name(self, value):
        return value.lower()
    

class FlagSerializer(serializers.ModelSerializer):
    keyword_name = serializers.CharField(source='keyword.name', read_only=True)
    content_title = serializers.CharField(source='content_item.title', read_only=True)
    class Meta:
        model = Flag
        fields = ['id', 'keyword', 'keyword_name', 'content_item', 'content_title', 'score', 'status']

