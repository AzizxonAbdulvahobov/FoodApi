from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class FoodTypeApiViewSet(viewsets.ModelViewSet):
    queryset = models.FoodType.objects.all()
    serializer_class = serializers.FoodTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def __str__(self) -> str:
        return self.name

class FoodApiViewSet(viewsets.ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def __str__(self) -> str:
        return self.name


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def __str__(self) -> str:
        return self.name