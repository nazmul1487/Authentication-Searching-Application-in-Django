from rest_framework import serializers
from search.models import UserInput


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['user', 'inputValue']

