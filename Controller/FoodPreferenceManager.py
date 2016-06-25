# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Controller.FoodPreferenceDBManager import FoodPreferenceDBManager


class FoodPreferenceManager(metaclass=Singleton):

    def __init__(self):
        self._foodPreferenceDBManger = FoodPreferenceDBManager()

    def getUserIDsByFoodID(self, foodID):
        '''
        해당 음식 ID를 이용하여 해당 음식을 선호하는 사용자의 목록을 반환
        :param foodID: 음식 ID (integer)
        :return: User ID(integer) (list)
        '''
        return self._foodPreferenceDBManger.searchUserIDsByFoodID(foodID)

    def getFoodPreferencesByUserID(self, userID):
        '''
        해당 사용자의 음식 선호를 반환
        :param userID: 사용자 ID (integer)
        :return: FoodPreference Class instances (list)
        '''
        return self._foodPreferenceDBManger.searchFoodPreferencesByUserID(userID)

    def getFoodPreferenceByUserIDAndFoodID(self, userID, foodID):
        '''
        해당 사용자가 평가했던 음식의 음식 선호를 반환
        :param userID: 사용자 ID (integer)
        :param foodID: 음식 ID (integer)
        :return: FoodPreference Class (instance)
        '''
        return self._foodPreferenceDBManger.searchFoodPreferenceByUserIDAndFoodID(userID, foodID)