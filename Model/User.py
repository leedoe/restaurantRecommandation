#-*- encoding=utf-8 -*-

from Model.FoodPreference  import FoodPreference
from Model.Food  import Food

class User:

    def __init__(self, email, password, age, gender):
        self._email = email
        self._password = password
        self._age = age
        self._gender = gender
        self._foodPreference = []

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
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age


    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @gender.deleter
    def gender(self):
        del self._gender


    @property
    def foodPreference(self):
        return self._foodPreference

    @foodPreference.setter
    def foodPreference(self,value):
        self._foodPreference = value

    @foodPreference.deleter
    def foodPreference(self):
        del self._foodPreference