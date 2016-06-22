# -*- encoding=utf-8 -*-

import copy
from Controller.FoodPreferenceManager import FoodPreferenceManager
from Controller.FoodManager import FoodManager
from math import exp

class RecommendationQueue:

    '''
    static 영역
    '''
    MAX_OF_GROUP_INFO = 5 # tuple에 넣어서 보여줄 그룹의 정보 최대 개수
    TOP = 1 # queue의 TOP이며, 코드에서 명시적으로 나타내기 위한 상수
    WEIGHT = {'SCORE': 4.0, 'ATTR': 3.0, 'MEAN': 2.0} # 추천 점수에 필요한 각 가중치, SCORE = 사용자가 준 평점, ATTR = 속성, MEAN = 총 평가 점수 평균
    GROUPINFO = {'NAME': 0, 'MEAN': 1, 'COUNT': 2, 'GROUPS': 3} # 큐에 저장되어 있는 tuple에 접근하기 위한 각 인덱스


    def __init__(self, user, foodSet, foodDict):
        '''
        음식 추천 Priority Queue를 초기화 해주는 생성자
        :param user: 추천을 요구하는 현재 사용자
        :param foodSet: 추천 가능성이 있는 음식들 이름의 Set
        :param foodDict: 추천 가능성이 있는 각 음식의 group 평가에 대한 Dictionaries
        '''
        self._foodPreferenceManager = FoodPreferenceManager()
        self._foodManager = FoodManager()

        # 각 음식을 하나씩 꺼내서 Queue에 넣는 작업을 한다.
        # 해당 Queue의 top은 [1]이다.
        self._queue = [('UNDERFLOW')]
        self._user = user

        # 추천 가능성이 있는 각 음식들을 queue에 넣는 작업을 시작함
        for food in foodSet:
            totalScore = totalCount = 0 # 해당 음식의 총점과 카운트는 0으로

            # 각 음식에 대한 평균과 모든 그룹의 총합, 카운트를 구함
            for groupInfo in foodDict[food]:
                totalScore += groupInfo[1]
                totalCount += groupInfo[2]
                groupInfo[1] /= groupInfo[2]

            foodDict[food].sort(key=lambda groupInfo : groupInfo[1], reverse=True) # 평균을 기준으로 내림차순으로 정렬
            del(foodDict[food][RecommendationQueue.MAX_OF_GROUP_INFO:]) # 최대 보여줄 그룹의 정보만 남김

            # 추천 정보는 tuple로 저장
            recommendationInfo = copy.copy((food, totalScore / totalCount, totalCount, foodDict[food]))
            self._add(recommendationInfo) # 추천 정보를 queue에 삽입




    def _add(self, recommendationInfo):
        '''
        queue에 음식 추천 정보를 저장한다.
        :param recommendationInfo: 음식 추천 정보 tuple
        :return: None
        '''

        self._queue.append(recommendationInfo) # queue에 추천 정보를 삽입
        cursor = len(self._queue) - 1 # 현재 음식 추천 정보를 가르키는 cursor

        while (cursor / 2) >= RecommendationQueue.TOP :
            if self._getRecommendationScore(self._queue[cursor]) > self._getRecommendationScore(self._queue[(cursor/2).__int__()]):
                self._swap(cursor, (cursor/2).__int__())
                cursor = (cursor / 2).__int__()
            else:
                break




    def _swap(self, idx1, idx2):
        '''
        queue 내부에서 서로의 원소를 교환한다.
        :param idx1: queue에서 교환할 index1
        :param idx2: queue에서 교환할 index2
        :return: None
        '''
        tmp = self._queue[idx1]
        self._queue[idx1] = self._queue[idx2]
        self._queue[idx2] = tmp




    def _getRecommendationScore(self, recommendationInfo):
        '''
        음식 추천 정보에 대해서 추천 점수를 계산하는 메소드
        :param recommendationInfo: 음식 추천 정보 tuple
        :return: 음식 추천 점수
        '''
        WEIGHT = RecommendationQueue.WEIGHT
        GROUPINFO = RecommendationQueue.GROUPINFO
        targetFoodAttribute = self._foodManager.getFoodAttributeByFoodName(recommendationInfo[GROUPINFO['NAME']]) # dictionaires
        userFoodPreferenceAttributes = self._foodManager.getFoodPreferenceAttributesByUserID(self._user.ID) # dictionaries의 list
        attributeNames = targetFoodAttribute.keys()

        score = 0.0

        #1. 유저가 평가한 음식의 속성, target 음식의 속성의 교집합의 합을 구함
        sumOfAttributesIntersection = 0
        for userFoodPreferenceAttribute in userFoodPreferenceAttributes:
            for attributeName in attributeNames:
                # 사용자 선호 음식과 target 음식의 속성들의 교집합 개수들의 합을 구함.
                if not userFoodPreferenceAttribute[attributeName] == None:
                    sumOfAttributesIntersection += userFoodPreferenceAttribute[attributeName] & targetFoodAttribute[attributeName]

        #2. 총 평가 점수와 그에 따른 패널티 적용
        penalty = 2.0 / (1.0 + exp(-0.05 * recommendationInfo[GROUPINFO['COUNT']]))
        targetFoodMean = recommendationInfo[GROUPINFO['MEAN']]


        #3. 사용자의 해당 음식에 대한 평가 점수가 존재할 시, 그에 대한 가산, 감산 점수
        #모델을 만들어야 함

        userAdditionalScore = 0.0

        #4. 추천 점수 계산
        score = WEIGHT['ATTR'] * sumOfAttributesIntersection + WEIGHT['MEAN'] * targetFoodMean * penalty + userAdditionalScore

        return score




    def pop(self):
        '''
        queue에서 음식 추천 정보를 반환하는 메소드
        :return: 음식 추천 정보 tuple ( food 이름, food 평점, food 평가 수, [그룹 별 food 평가 점수 및 평가 개수])
        '''
        result = copy.copy(self._queue[RecommendationQueue.TOP])

        cursor = RecommendationQueue.TOP # 계속적으로 음식 추천 정보를 교환할 것을 가르키는 cursor
        self._queue[RecommendationQueue.TOP] = copy.copy(self._queue[len(self._queue) - 1])
        del(self._queue[len(self._queue) - 1])


        while 2 * cursor < len(self._queue):
            # 1. 오른쪽 자식이 존재하고, 오른쪽 자식이 왼쪽 자식의 점수보다 크고, 오른쪽 자식이 부모의 점수보다 클 경우
            if (2 * cursor + 1 < len(self._queue)) \
                and (self._getRecommendationScore(2 * cursor + 1) > self._getRecommendationScore(2 * cursor)) \
                and (self._getRecommendationScore(2 * cursor + 1) > self._getRecommendationScore(cursor)):
                self._swap(cursor, 2 * cursor + 1)
                cursor = 2 * cursor + 1
            # 2. 1이 아닐 때, 왼쪽 자식이 부모의 점수보다 클 경우
            elif self._getRecommendationScore(2 * cursor) > self._getRecommendationScore(cursor):
                self._swap(cursor, 2 * cursor)
                cursor = 2 * cursor
            # 3. 부모가 자식보다 점수가 클 경우
            else:
                break

        return result









