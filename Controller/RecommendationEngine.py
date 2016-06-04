#-*- encoding=utf-8 -*-

from Controller.UserManager import UserManager
from Controller.FoodManager import FoodManager
from Controller.FoodPreferenceManager import FoodPreferenceManager
from Controller.RestaurantManager import RestaurantManager
from Model.Singleton import Singleton
from Model.FoodPreference import FoodPreference

## 파이썬은 getter/setter대신 properties를 사용한다고 함.
## 해당 방법에 대해서 알아봐야 함.
## 일단은 getter를 사용하지 않고 코드 작성

class RecommendationEngine:
    __metaclass__ = Singleton

    def __init__(self):
        self._userManager = UserManager()
        self._foodManager = FoodManager()
        self._foodPreferenceManager = FoodPreferenceManager()
        self._restaurantManager = RestaurantManager()

    def runMapping(self, user):
        userPreferences = user.getFoodPreferences().sort(reverse = True, key = FoodPreference._score)

        # 추천을 받고자 하는 사용자가 평가한 음식들의 평균 점수를 구한다.
        total = 0
        for preference in userPreferences: # 해당 부분을 User쪽에 넣는거 생각하기
            total = preference.getScore()
        mean = total / len(userPreferences)

        # 사용자가 평가한 음식 중 평균이 넘는 음식에 대해서 타 사용자 선호 조사
        for foodPreference in userPreferences:
            otherUsersPreference = self._foodPreferenceManager.getUsersByFoodName(foodPreference._food)
            result = self._countAndCalculateMean(otherUsersPreference)
            # 데이터 저장 방식은????




    def _isAlreadyEvaluated(self):
        pass

    def _calculateFoodRecommendation(self):
        pass

    def _countAndCalculateMean(self, otherUserPreferenceList):
        pass

    def _addRestaurantList(self):
        pass
