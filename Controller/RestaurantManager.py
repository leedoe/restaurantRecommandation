# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Restaurant import Restaurant
from Model.RestaurantList import RestaurantList
from Controller.RestaurantDBManager import RestaurantDBManager

#식당 객체를 관리하는 매니저 클래스
class RestaurantManager:
    __metaclass__ = Singleton

    def __init__(self):
        self._restaurantList = []
        self._restaurantDBManager = RestaurantDBManager()

    def addRestaurant(self,name,location,foods):
        restaurant = Restaurant(name, location, foods)
        self.restaurantList.restaurantList.append(restaurant)

    def modifyRestaurantByName(self, name, newName):
        for restaurant in self.restaurantList.restaurantList:
            if (restaurant.getName() == name):
                restaurant.setName(newName)
                break

    def modifyRestaurantByLocation(self,name,location):
        for restaurant in self.restaurantList.restaurantList:
            if(restaurant.getName() == name):
                restaurant.setLocation(location)
                break

    def modifyRestaurantByFoods(self, name, foods):
        for restaurant in self.restaurantList.restaurantList:
            if (restaurant.getName() == name):
                restaurant.setFoods(foods)
                break

    def deleteRestaurantByName(self,name):
        for restaurant in self.restaurantList.restaurantList:
            if (restaurant.getName() == name):
                self.restaurantList.restaurantList.remove(restaurant)
                break


    @property
    def restaurantList(self):
        return self._restaurantList

    @restaurantList.setter
    def restaurantList(self, value):
        self._restaurantList = value

    @restaurantList.deleter
    def restaurantList(self):
        del self._restaurantList


    @property
    def restaurantDBManager(self):
        return self._restaurantDBManager

    @restaurantDBManager.setter
    def restaurantDBManager(self, value):
        self._restaurantDBManager = value

    @restaurantDBManager.deleter
    def restaurantDBManager(self):
        del self._restaurantDBManager