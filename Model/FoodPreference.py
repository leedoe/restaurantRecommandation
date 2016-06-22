#-*- encoding=utf-8 -*-

#음식선호도에 대한 정보를 담고 있는 클래스
class FoodPreference:
    #멤버변수:음식 이름,점수
    def __init__(self, ID, score, userID, foodID):
        self._ID = ID
        self._score = score
        self._userID = userID
        self._foodID = foodID

    #음식선호도 객체 정보를 출력
    def __repr__(self):
        return "FoodPreference{음식명=%s ,선호도 점수=%d}"%(self._foodName,self._score)

    @property
    def ID(self):
        return self._ID

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score = value

    @property
    def userID(self):
        return self._userID

    @property
    def foodID(self):
        return self._foodID