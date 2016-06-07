# -*- encoding=utf-8 -*-

import copy

class RecommendationQueue:

    MAX_OF_GROUP_INFO = 5 # 최대 보여줄 그룹의 정보
    TOP = 1 # queue의 TOP이며, 코드에서 명시적으로 나타내기 위한 상수

    def __init__(self, user, foodSet, foodDict):
        '''
        음식 추천 Priority Queue를 초기화 해주는 생성자
        :param user: 추천을 요구하는 현재 사용자
        :param foodSet: 추천 가능성이 있는 음식들 이름의 Set
        :param foodDict: 추천 가능성이 있는 각 음식의 group 평가에 대한 Dictionaries
        '''

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
        pass




    def pop(self):
        '''
        queue에서 음식 추천 정보를 반환하는 메소드
        :return: 음식 추천 정보 tuple
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









