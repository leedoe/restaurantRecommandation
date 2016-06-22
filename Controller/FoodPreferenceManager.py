# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Controller.FoodPreferenceDBManager import FoodPreferenceDBManager


#음식선호도 객체를 관리하는 매니저 클래스
class FoodPreferenceManager(metaclass=Singleton):

    def __init__(self):
        self._foodPreferenceDBManger = FoodPreferenceDBManager()

    def getUserIDsByFoodID(self, foodID):
        '''
        해당 음식 ID를 이용하여 해당 음식을 선호하는 사용자의 목록을 반환
        :param foodID: 음식 ID
        :return: User ID(integer)의 list
        '''
        return self._foodPreferenceDBManger.searchUserIDsByFoodID(foodID)

    def getFoodPreferencesByUserID(self, userID):
        '''
        해당 사용자의 음식 선호를 반환
        :param userID: 사용자ID
        :return: FoodPreference instance의 list
        '''
        return self._foodPreferenceDBManger.searchFoodPreferencesByUserID(userID)