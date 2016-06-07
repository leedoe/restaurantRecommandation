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
        userPreferences = user.getFoodPreferences().sort(key = lambda FoodPreference: FoodPreference._score, reverse = True)
        foodSet = set()
        foodDict = dict()

        # 추천을 받고자 하는 사용자가 평가한 음식들의 평균 점수를 구한다.
        total = 0
        for preference in userPreferences: # 해당 부분을 User쪽에 넣는거 생각하기
            total = preference.getScore()
        mean = total / len(userPreferences)

        # 사용자가 평가한 음식 중 평균이 넘는 음식에 대해서 타 사용자 선호 조사
        for foodPreference in userPreferences:
            if foodPreference._score < mean: break # 평균보다 낮은 점수면 루프에서 나감
            otherUsers = self._foodPreferenceManager.getUsersByFoodName(foodPreference._food)
            self._countAndCalculateMean(otherUsers, foodPreference, foodSet, foodDict)

        #여기서 priority queue화를 한다.




    def _isAlreadyEvaluated(self):
        pass

    def _calculateFoodRecommendation(self):
        pass

    ## _countAndCalculateMean
    # 다른 유저들의 선호도를 모두 체크하여 총 평균과 카운트를 계산함
    # dictionary value의 구성 : [[group, 평균, count], [group, 평균, count], ...]]
    # group에 대한 평균과 count는 Priority Queue에 넣기 전에는 항상 총점으로 두고 Queue에 넣은 후에는 평균으로 바꾼다.
    # 왜냐하면 이곳에서 계속해서 평균을 계산할 필요가 없기 때문이다.
    # value를 tuple로 사용하지 않은 이유는 tuple은 변경할 수 없는 데이터 형이기 때문
    def _countAndCalculateMean(self, otherUsers, foodPreference, foodSet, foodDict):
        # 각 다른 사용자들에 대한 음식 선호도를 불러옴
        for otherUser in otherUsers:
            otherUserPreferences = self._foodPreferenceManager.getFoodsByUserID(otherUser) # 다른 사용자 한 명의 음식 선호 평가를 불러옴


            for otherUserPreference in otherUserPreferences:
                foodSet.add(otherUserPreference._food) # 음식 이름을 set에 추가

                if not foodDict.get(otherUserPreference._food): # 해당 음식이 dictionaries에 존재하지 않을 경우
                    foodDict[otherUserPreference._food] = [0, 0, [[foodPreference._food, otherUserPreference._score, 1]]] # 새로운 원소를 하나 생성함
                else: # 해당 음식이 dictionaries에 존재할 경우
                    # 다른 사용자가 아닌 현재 사용자(나)가 평가한 음식의 그룹이 존재하지 않으면
                    if not foodDict[otherUserPreference._food][-1][-1][0] == foodPreference._food:
                        foodDict[otherUserPreference._food][-1].add([foodPreference._food, otherUserPreference._score, 1]) # 새로운 그룹을 생성
                    else : # 음식의 그룹이 존재할 경우 총 점수와 카운트를 증가시킴
                        foodDict[otherUserPreference._food][-1][1] += otherUserPreference._score
                        foodDict[otherUserPreference._food][-1][2] += 1


    def _addRestaurantList(self):
        pass
