#-*- encoding=utf-8 -*-

from Model.FoodPreference  import FoodPreference
from Model.Food  import Food

class User:

    def __init__(self, email, password, age, gender):
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.foodPreference = []

    def addPreference(self, foodName, score):
        food = Food(foodName)
        foodPreference = FoodPreference(score, food)
        self.foodPreference.append(foodPreference)

    def modifyPreference(self, foodName, score):
        for foodPreference in self.foodPreference:
            food = foodPreference.getFood()
            if food.getName() == foodName:
                food.setScore(score)
                break


    def deletePreference(self, foodName):
        for foodPreference in self.foodPreference:
            food = foodPreference.getFood()
            if food.getName() == foodName:
                self.foodPreference.remove(foodPreference)
                break

    @property
    def getFoodPreference(self):
        return self.foodPreference

    @property
    def getUserId(self):
        return self.userId

    @property
    def getEmail(self):
        return self.email

    @property
    def getPassword(self):
        return self.password

    @property
    def getAge(self):
        return self.age

    @property
    def getGender(self):
        return self.gender

    @property
    def getFoodPreference(self):
        return self.foodPreference

    def setUserId(self,userId):
        self.userId = userId

    def setEmail(self,email):
        self.email = email

    def setPassword(self,password):
        self.password = password

    def setAge(self,age):
        self.age = age

    def setGender(self,gender):
        self.gender = gender

    def setFoodPreference(self,foodPreference):
        self.foodPreference = foodPreference