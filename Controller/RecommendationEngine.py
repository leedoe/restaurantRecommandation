# -*- encoding=utf-8 -*-

from Controller.UserManager import UserManager
from Controller.FoodManager import FoodManager
from Controller.FoodPreferenceManager import FoodPreferenceManager
from Controller.RestaurantManager import RestaurantManager
from Controller.RecommendationQueue import RecommendationQueue
from Model.Singleton import Singleton
from Model.FoodPreference import FoodPreference

# 파이썬은 getter/setter대신 properties를 사용한다고 함.
# 해당 방법에 대해서 알아봐야 함.
# 일단은 getter를 사용하지 않고 코드 작성

class RecommendationEngine:
    __metaclass__ = Singleton

    def __init__(self):
        '''
        추천 엔진에 필요한 Manager를 부르는 생성자
        '''
        self._userManager = UserManager()
        self._foodManager = FoodManager()
        self._foodPreferenceManager = FoodPreferenceManager()
        self._restaurantManager = RestaurantManager()




    def runMapping(self, user):
        '''
        음식 선호와 식당의 교집합을 mapping해주는 메소드
        :param user: User 클래스의 instance
        :return: 교집합의 리스트
        '''

        foodRecommendationQueue = self._getFoodRecommendationQueue(user)




    def _getFoodRecommendationQueue(self, user):
        '''
        음식 추천 queue를 생성하는 메소드
        :param user: 음식 추천 queue를 생성할 User클래스의 instance
        :return: RecommendationQueue 클래스의 instance
        '''
        userPreferences = user.getFoodPreferences().sort(key=lambda FoodPreference: FoodPreference._score, reverse=True)
        foodSet = set()
        foodDict = dict()

        # 추천을 받고자 하는 사용자가 평가한 음식들의 평균 점수를 구한다.
        total = 0
        for preference in userPreferences:  # 해당 부분을 User쪽에 넣는거 생각하기
            total = preference.getScore()
        mean = total / len(userPreferences)

        # 사용자가 평가한 음식 중 평균이 넘는 음식에 대해서 타 사용자 선호 조사
        for foodPreference in userPreferences:
            if foodPreference._score < mean: break  # 평균보다 낮은 점수면 루프에서 나감
            otherUsers = self._foodPreferenceManager.getUsersByFoodName(foodPreference._food)
            self._countAndCalculateMean(otherUsers, foodPreference, foodSet, foodDict)

        # 여기서 priority queue화를 한다.
        recommenationQueue = RecommendationQueue(user, foodSet, foodDict)

        #메모리에서 해당 data들을 명시적으로 없애줌.
        del(foodSet)
        del(foodDict)

        return recommenationQueue




    def _countAndCalculateMean(self, otherUsers, foodPreference, foodSet, foodDict):
        '''
        다른 유저들의 선호도를 모두 체크하여 각 음식 그룹 점수의 총합과 평가한 사용자의 카운트를 계산하는 메소드
        해당 메소드는 private 형태이며, 내부에서 쓰이는 데이터는 다음과 같다.
        foodSet : 추천 가능성이 있는 음식 이름의 Set
        foodDict : 추천 가능성이 있는 음식에 대해서 각 음식을 평가한 그룹이 평가한 점수의 총합과 카운트를 저장하는 Dictionaries
        foodDict.Key = '음식이름'(str)
        foodDict.value = [[group이름, 점수 총합, 평가한 총인원], [group이름, 점수 총합, 평가한 총인원], ...]
        (점수 총합을 저장하는 이유는 평균을 지속적으로 유지하기 위해서는 추가할 때 마다 연산을 해야 하기 때문이다.)
        :param otherUsers: 해당 음식을 평가한 다른 유저(User클래스의 instance를 원소로 갖는 list)
        :param foodPreference: 추천을 요구하는 사용자의 해당 음식 취향
        :param foodSet: 추천 가능성이 있는 음식 이름의 set
        :param foodDict: 추천 가능성이 있는 음식의 각 group별 점수 총합, 평가 총인원 dictionaries
        :return: None
        '''
        # 각 다른 사용자들에 대한 음식 선호도를 불러옴
        for otherUser in otherUsers:
            otherUserPreferences = self._foodPreferenceManager.getFoodsByUserID(otherUser) # 다른 사용자 한 명의 음식 선호 평가를 불러옴


            for otherUserPreference in otherUserPreferences:
                foodSet.add(otherUserPreference._food) # 음식 이름을 set에 추가

                if not foodDict.get(otherUserPreference._food): # 해당 음식이 dictionaries에 존재하지 않을 경우
                    foodDict[otherUserPreference._food] = [[foodPreference._food, otherUserPreference._score, 1]] # 새로운 원소를 하나 생성함
                else: # 해당 음식이 dictionaries에 존재할 경우
                    # 다른 사용자가 아닌 현재 사용자(나)가 평가한 음식의 그룹이 존재하지 않으면
                    if not foodDict[otherUserPreference._food][-1][0] == foodPreference._food:
                        foodDict[otherUserPreference._food].append([foodPreference._food, otherUserPreference._score, 1]) # 새로운 그룹을 생성
                    else : # 음식의 그룹이 존재할 경우 총 점수와 카운트를 증가시킴
                        foodDict[otherUserPreference._food][-1][1] += otherUserPreference._score
                        foodDict[otherUserPreference._food][-1][2] += 1




    def _isAlreadyEvaluated(self):
        pass




    def _calculateFoodRecommendation(self):
        pass




    def _addRestaurantList(self):
        pass