# -*- encoding=UTF-8 -*-

from Model.GroupInfo import GroupInfo

class RecommendationInfo:

    MAX_OF_GROUP_INFO = 5 # groupInfo에 남길 group 정보의 최대 개수

    def __init__(self, foodID, groupID, mean, count):
        '''
        RecommendationQueue에 들어갈 element 클래스
        :param groupID: 음식을 평가한 그룹의 음식 ID (integer)
        :param mean: 점수이며 나중에 평균으로 바뀜 (integer)
        :param count: 음식을 평가한 그룹의 사용자 총 인원 (integer)
        '''
        self.foodID = foodID
        self.mean = float()
        self.count = int()
        self.score = None
        self.groupInfos = []
        self.addGroupInfo(groupID, mean, count)

    def __repr__(self):
        groupInfos = ''
        for groupInfo in self._groupInfos:
            groupInfos += groupInfo.__repr__() + ', '
        groupInfos = groupInfos[:-2]

        return "RecommendationInfo(foodID = %d, mean = %f, count = %d, score = %f, groupInfos = [%s])"\
               %(self.foodID, self.mean, self.count, self.score, groupInfos)

    def addGroupInfo(self, groupID, mean, count):
        '''
        해당 음식을 평가한 음식 그룹을 추가시켜줌
        :param groupID: 추가할 음식 그룹 ID (integer)
        :param mean: 초기 점수 (integer)
        :param count: 초기 카운트 (integer)
        :return:
        '''
        self._groupInfos.append(GroupInfo(groupID, mean, count))

    def rstripGroupInfos(self):
        '''
        해당 음식을 평가한 그룹을 MAX_OF_GROUP_INFO만큼 잘라줌
        :return: None
        '''
        del self.groupInfos[self.MAX_OF_GROUP_INFO:]

    def sortGroupInfos(self, descending):
        '''
        해당 음식을 평가한 그룹을 평균을 기준으로 정렬해줌
        :param ascending: T/F (boolean)
        :return: None
        '''
        self.groupInfos = sorted(self.groupInfos, key= lambda groupInfo : groupInfo.mean, reverse= descending)

    @property
    def foodID(self):
        return self._foodID

    @foodID.setter
    def foodID(self, foodID):
        self._foodID = foodID

    @foodID.deleter
    def foodID(self):
        del self._foodID

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
    def count(self, value):
        self._count = value

    @count.deleter
    def count(self):
        del self._count

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @score.deleter
    def score(self):
        del self._score

    @property
    def groupInfos(self):
        return self._groupInfos

    @groupInfos.setter
    def groupInfos(self, groupInfos):
        self._groupInfos = groupInfos

    @groupInfos.deleter
    def groupInfos(self):
        del self._groupInfos

    @property
    def latestGroupInfo(self):
        return self._groupInfos[-1]
