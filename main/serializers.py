from rest_framework import serializers
from . import models


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodType
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'