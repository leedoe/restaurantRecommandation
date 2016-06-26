# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Restaurant import Restaurant
from Controller.RestaurantDBManager import RestaurantDBManager

#식당 객체를 관리하는 매니저 클래스
class RestaurantManager(metaclass=Singleton):

    def __init__(self):
        self._restaurantDBManager = RestaurantDBManager()

    def getRestaurantIDsByFoodID(self, foodID):
        '''
        음식 ID를 이용하여 해당 음식을 메뉴로 갖고 있는 식당 ID를 얻음
        :param foodID: 음식 ID (integer)
        :return: 식당 ID 목록 (list)
        '''
        return self._restaurantDBManager.searchRestaurantsIDsByFoodID(foodID)

    def getRestaurantsByRestaurantID(self, restaurantID):
        '''
        식당 ID를 이용하여 해당 음식의 정보를 얻음
        :param restaurantID: 식당 ID (integer)
        :return: Restaurant Class instances (list)
        '''
        return self._restaurantDBManager.searchRestaurantsByRestaurantID(restaurantID)

    def getRestaurantsByRestaurantIDAndLocation(self, restaurantID, location):
        '''
        식당 ID와 지역을 이용하여 해당 음식의 정보를 얻음
        :param restaurantID: 식당 ID (integer)
        :param location: 지역 (string)
        :return: Restaurant Class instances (list)
        '''
        return self._restaurantDBManager.searchRestaurantsByRestaurantIDAndLocation(restaurantID, location)

    def getRestaurantFeaturesByRestaurantID(self, restaurantID):
        '''
        식당 ID를 이용하여 해당 식당 특징을 얻어옴
        :param restaurantID: 식당 ID (integer)
        :return: RestaurantFeature Class instances (list)
        '''
        return self._restaurantDBManager.searchRestaurantFeaturesByRestaurantID(restaurantID)