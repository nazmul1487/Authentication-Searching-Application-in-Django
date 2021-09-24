import pytz
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response

from authentication.models import User
from django.core import serializers
from search.models import UserInput
from restapi.serializers import SearchSerializer
from search.models import UserInput
from datetime import datetime
import datetime
# Create your views here.


class SearchView(generics.GenericAPIView):
    serializer_class = SearchSerializer
    # value = UserInput.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET['start_datetime'] and request.GET['end_datetime'] and request.GET['user_id']:
            start_datetime = request.GET['start_datetime']
            end_datetime = request.GET['end_datetime']
            start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
            end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
            # print(start_datetime)
            user_id = (request.GET['user_id'])
            queryset = UserInput.objects.filter(user_id=user_id, timestamp__gte=start_datetime, timestamp__lte=end_datetime)
            serializer = SearchSerializer(queryset, many=True)
            # print(serializer.data)
            response = {
                'status': 'success',
                'user_id': user_id,
                'payload': serializer.data
            }
            return Response(response, content_type="application/json")
        message = 'Something is wrong'
        response = {
            'status': 'Bad Request',
            'message': message
        }
        return Response(response, content_type="application/json")
