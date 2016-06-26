# -*- encoding=UTF-8 -*-

class GroupInfo:

    def __init__(self, ID, mean, count):
        '''
        RecommendationQueue의 Element가 되는
        RecommendationInfo 클래스에 들어갈 음식을 평가한 그룹에 관한 정보 클래스
        :param ID: 음식을 평가한 음식 그룹 ID (integer)
        :param score: 음식을 평가한 음식 그룹의 점수 (integer)
        :param count: 음식을 평가한 음식 그룹의 인원 (integer)
        '''
        self.ID = ID
        self.mean = mean
        self.count = count

    def __repr__(self):
        return "GroupInfo(ID = %d, mean = %f, count = %d)"%(self.ID, self.mean, self.count)

    def addScore(self, score):
        '''
        그룹의 음식 평가 점수를 더해줌
        :param score: 더할 점수
        :return: None
        '''
        self.mean += score

    def incrementCount(self):
        '''
        음식 평가 수를 1 증가시켜줌
        :return: None
        '''
        self.count += 1

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @ID.deleter
    def ID(self):
        del self._ID

    @property
    def mean(self):
        return self._mean

    @mean.setter
    def mean(self, mean):
        self._mean = mean

    @mean.deleter
    def mean(self):
        del self._mean

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @count.deleter
    def count(self):
        del self._count
