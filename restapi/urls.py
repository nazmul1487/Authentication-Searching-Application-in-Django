from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapi import views

router = DefaultRouter()


urlpatterns = [
    path('', views.SearchView.as_view()),
]