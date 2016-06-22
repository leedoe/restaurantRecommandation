from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# UserInformation
class UserInfo(AbstractUser):
    age = models.IntegerField(null=False)
    location = models.CharField()

    def __str__(self):
        return self.username


# Food Information
class Food(models.Model):
    name = models.CharField(null=False)

    def __str__(self):
        return self.name


# Food Attribute
class FoodAttribute(models.Model):
    foodID = models.ForeignKey(Food)
    attributeName = models.CharField()
    contents = models.CharField()

    def __str__(self):
        return str(self.foodID) + " " + self.attributeName


# User Preference
class UserFoodPreference(models.Model):
    userID = models.ForeignKey(UserInfo)
    foodID = models.ForeignKey(Food)
    score = models.FloatField()

    def __str__(self):
        return str(self.userID) + " " + str(self.foodID)


# Restaurant
class Restaurant(models.Model):
    name = models.CharField()
    location = models.CharField()

    def __str__(self):
        return self.name


# Restaurant Score by User
class RestaurantScore(models.Model):
    userID = models.ForeignKey(UserInfo)
    restaurantID = models.ForeignKey(Restaurant)
    score = models.FloatField()

    def __str__(self):
        return str(self.userID) + " " + str(self.restaurantID)