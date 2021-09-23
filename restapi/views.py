from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response
from search.models import UserInput
from restapi.serializers import SearchSerializer

# Create your views here.


class SearchView(generics.GenericAPIView):
    serializer_class = SearchSerializer

    def post(self, request, *args, **kwargs):
        print(request.GET)
        return Response()
