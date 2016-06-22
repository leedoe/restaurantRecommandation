# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Restaurant import Restaurant
from Model.RestaurantList import RestaurantList
from Controller.RestaurantDBManager import RestaurantDBManager

#식당 객체를 관리하는 매니저 클래스
class RestaurantManager:
    __metaclass__ = Singleton
    # 멤버변수:식당 객체 리스트 객체,식당db매니저 객체
    def __init__(self):
        self._restaurantList = RestaurantList()
        self._restaurantDBManager = RestaurantDBManager()

    #식당정보로 식당객체 리스트에 추가
    def addRestaurant(self,id,name,location,foods):
        restaurant = Restaurant(id,name, location)
        restaurant.foods = foods
        self.restaurantList.addRestaurant(restaurant)

    #식당 이름 변경
    def modifyRestaurantByName(self, name, newName):
        return self.restaurantList.modifyRestaurantByName(name,newName)

    #식당 주소 변경
    def modifyRestaurantByLocation(self,name,location):
        return self.restaurantList.modifyRestaurantByLocation(name,location)

    #식당 음식들 변경
    def modifyRestaurantByFoods(self, name, foods):
        return self.restaurantList.modifyRestaurantByFoods(name,foods)

    #식당 삭제
    def deleteRestaurantByName(self,name):
        return self.restaurantList.deleteRestaurantByName(name)


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