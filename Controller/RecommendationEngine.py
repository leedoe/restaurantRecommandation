#-*- encoding=utf-8 -*-

from Controller.FoodManager import FoodManager
from Controller.RestaurantManager import RestaurantManager
from Controller.UserManager import UserManager
from Model.Singleton import Singleton


class RecommendationEngine:
    __metaclass__ = Singleton

    def __init__(self):
        self._foodManager = FoodManager()
        self._restaurantManager = RestaurantManager()
        self._userManager = UserManager()

    def runMapping(self, user):
        pass

    def isAlreadyEvaluated(self):
        pass

    def calculateFoodRecommendation(self):
        pass

    def countAndCalculateMean(self):
        pass

    def addRestaurantList(self):
        pass
