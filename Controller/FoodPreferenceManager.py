# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Controller.FoodPreferenceDBManager import FoodPreferenceDBManager


#음식선호도 객체를 관리하는 매니저 클래스
class FoodPreferenceManager:
    __metaclass__ = Singleton

    def __init__(self):
        self._foodPreferenceDBManger = FoodPreferenceDBManager()

    def getUsersByFoodName(self, foodName):
        self._foodPreferenceDBManger.searchUsersByFoodName(foodName)
        return

    def getFoodsByUserID(self, userID):
        self._foodPreferenceDBManger.searchFoodsByUserID(userID)
        return