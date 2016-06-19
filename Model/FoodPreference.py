#-*- encoding=utf-8 -*-

#음식선호도에 대한 정보를 담고 있는 클래스
class FoodPreference:
    #멤버변수:음식 이름,점수
    def __init__(self, foodName, score):
        self._foodName = foodName
        self._score = score

    @property
    def foodName(self):
        return self._foodName

    @foodName.setter
    def foodName(self,value):
        self._foodName = value

    @foodName.deleter
    def foodName(self):
        del self._foodName


    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score = value

    @score.deleter
    def score(self):
        del self._score

