# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Food import Food
from Controller.FoodDBManager import FoodDBManager


class FoodManager(metaclass=Singleton):

    def __init__(self):
        self._foodDBManager = FoodDBManager()

    def getFoodAttributesByFoodID(self, foodID):
        '''
        음식 ID(integer)를 이용하여 음식의 속성을 반환
        :param foodID: 음식 ID (integer)
        :return: 해당 음식의 속성 (dictionaries)
        '''
        return self._foodDBManager.searchFoodAttributesByFoodID(foodID)


    def getPreferencedFoodAttributesListByUserID(self, userID):
        '''
        사용자 ID(integer)를 이용하여 사용자 선호 음식들의 속성을 반환
        dictionary 들의 list로 반환하지만, 해당 element가 어떤 음식인지는 알 수 없음
        :param userID: 사용자의 ID (integer)
        :return: 해당 사용자의 선호 음식의 속성 dictionary (list)
        '''
        return self._foodDBManager.searchPreferencedFoodAttributesListByUserID(userID)


    def getFoodAttributeWeights(self):
        '''
        각 음식 속성에 대한 가중치를 반환
        :return: 음식 속성 가중치 (dictionary)
        '''
        return self._foodDBManager.searchFoodAttributeWeights()
