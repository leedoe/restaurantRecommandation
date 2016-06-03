#-*- encoding=utf-8 -*-

from Model.Singleton import Singleton

class RestaurantManager:
    __metaclass__ = Singleton

    def __init__(self):
        self._restaurantList = []
        self._restaurantDBManager
        pass

    def addRestaurant(self):
        pass

    def modifyRestaurant(self):
        pass

    def deleteRestaurant(self):
        pass

    def getRestaurantByLocationAndFood(self):
        pass