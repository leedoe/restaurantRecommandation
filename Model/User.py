#-*- encoding=utf-8 -*-

from Model.FoodPreference  import FoodPreference

#유저에 대한 정보를 담고 있는 클래스
class User:
    # 멤버변수:유저 이메일,비밀번호,나이,성별,음식 선호도
    def __init__(self, email, password, age, gender):
        self._email = email
        self._password = password
        self._age = age
        self._gender = gender
        self._foodPreference = []

    #음식 선호도를 추가하는 함수
    def addPreference(self, foodName, score):
        #food 이름 중복 검사
        for foodPreference in self._foodPreference:
            if foodPreference.foodName == foodName:
                return False
        foodPreference = FoodPreference(foodName, score)
        self._foodPreference.append(foodPreference)
        return True

    # 음식 선호도를 음식 이름을 기준으로 점수를 변경하는 함수
    def modifyPreference(self, foodName, score):
        for foodPreference in self._foodPreference:
            if foodPreference.foodName == foodName:
                foodPreference.score = score
                return True
        return False

    #음식 선호도에서 음식이름을 기준으로 제거하는 함수
    def deletePreference(self, foodName):
        for foodPreference in self._foodPreference:
            if foodPreference.foodName == foodName:
                self._foodPreference.remove(foodPreference)
                return True
        return False

    #유저객체 정보를 출력
    def __repr__(self):
        return "User{이메일=%s ,비밀번호=%s ,나이=%d ,성별=%s ,음식선호도 개수=%d}"%(self._email,self._password,self._age,self._gender,len(self._foodPreference))

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age


    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @gender.deleter
    def gender(self):
        del self._gender


    @property
    def foodPreference(self):
        return self._foodPreference

    @foodPreference.setter
    def foodPreference(self,value):
        self._foodPreference = value

    @foodPreference.deleter
    def foodPreference(self):
        del self._foodPreference