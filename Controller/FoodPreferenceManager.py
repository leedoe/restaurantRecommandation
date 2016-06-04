#-*- encoding=utf-8 -*-

from Model.Singleton import Singleton

class FoodPreferenceManager:
    __metaclass__ = Singleton

    def __init__(self):
        self.foodPreferenceDBManager

    def getUsersByFoodName(self):
        pass

    def getFoodsByUserID(self):
        pass