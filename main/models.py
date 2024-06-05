from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FoodType(models.Model):
    name = models.CharField(max_length=255)


class Food(models.Model):
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tarkibi  = models.TextField()
    narxi = models.FloatField()


class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    