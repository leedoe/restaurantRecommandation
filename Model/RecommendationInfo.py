# -*- encoding=UTF-8 -*-

class RecommendationInfo:

    def __init__(self, groupID, mean, count):
        '''
        RecommendationQueue에 들어갈 element
        :param groupID: 음식을 평가한 그룹의 음식 ID (integer)
        :param mean: 점수이며 나중에 평균으로 바뀜 (integer)
        :param count: 음식을 평가한 그룹의 사용자 총 인원 (integer)
        '''
        self._foodID = int()
        self._mean = float()
        self._count = int()
        self._score = None
        self._groupInfos = []
        self.addGroupInfo(groupID, mean, count)

    def addGroupInfo(self, groupID, mean, count):
        self._groupInfos.append([groupID, mean, count])

    @property
    def foodID(self):
        return self._foodID

    @property
    def mean(self):
        return self._mean

    @property.setter
    def mean(self, value):
        self._mean = value

    @property
    def count(self):
        return self._count

    @property.setter
    def count(self, value):
        self._count = value

    @property
    def score(self):
        return self._score

    @property.setter
    def score(self, value):
        self._score = value

    @property
    def groupInfos(self):
        return self._groupInfos
