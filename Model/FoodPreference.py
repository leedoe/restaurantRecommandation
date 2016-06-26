#-*- encoding=utf-8 -*-


class FoodPreference:

    def __init__(self, ID, score, userID, foodID):
        '''
        음식 선호에 관한 정보를 가지고 있는 클래스
        :param ID: 선호 음식 ID (integer)
        :param score: 선호 음식에 관한 점수 (integer)
        :param userID: 평가한 사용자 ID (integer)
        :param foodID: 평가받은 음식 ID (integer)
        '''
        self.ID = ID
        self.score = score
        self.userID = userID
        self.foodID = foodID

    def __repr__(self):
        return "FoodPreference(ID = %d, score = %f, userID = %d, foodID = %d)"%(self.ID, self.score, self.userID, self.foodID)

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
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score = value

    @score.deleter
    def score(self):
        del self._score

    @property
    def userID(self):
        return self._userID

    @userID.setter
    def userID(self, userID):
        self._userID = userID

    @userID.deleter
    def userID(self, userID):
        del self._userID

    @property
    def foodID(self):
        return self._foodID

    @foodID.setter
    def foodID(self, foodID):
        self._foodID = foodID

    @foodID.deleter
    def foodID(self):
        del self._foodID