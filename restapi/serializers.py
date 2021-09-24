from rest_framework import serializers
from search.models import UserInput


class SearchSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    inputValue = serializers.CharField(max_length=200)




