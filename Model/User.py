#-*- encoding=utf-8 -*-

from Model.FoodPreference  import FoodPreference

#유저에 대한 정보를 담고 있는 클래스
class User:
    # 멤버변수:유저 이메일,비밀번호,나이,성별,음식 선호도
    def __init__(self, email, password, age, gender):
        self._ID = int()
        self._email = str()
        self._password = str()
        self._age = int()
        self._gender = gender


    #유저객체 정보를 출력
    def __repr__(self):
        return "User{사용자ID=%d, 이메일=%s ,비밀번호=%s ,나이=%d"%(self._ID, self._email,self._password,self._age)


    @property
    def ID(self):
        return self._ID


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