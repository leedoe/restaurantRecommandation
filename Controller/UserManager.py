# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.User import User
from Controller.UserDBManager import UserDBManger

#유저 객체를 관리하는 매니저 클래스
class UserManager:
    __metaclass__ = Singleton

    def __init__(self):
        self._userDBManager = UserDBManger()

    def searchUserByEmail(self,email):
        self._userDBManger.searchUser()

    #유저 객체를 생성한다음에 db에 저장
    def makeUser(self,email,password,age,gender):
        self._user = User(email, password, age, gender)
        self._userDBManger.insertUser(self._user)

    def modifyUser(self,email,password):
        self._userDBManger.modifyUser()

    def deleteUser(self,email,password):
        self._userDBManger.deleteUser()

    def getUserPreferences(self,user):
        user = self._userDBManger.searchUser()
        return user.foodPreference

    @property
    def userDBManger(self):
        return self._userDBManger

    @userDBManger.setter
    def userDBManger(self,value):
        self._userDBManger = value

    @userDBManger.deleter
    def userDBManger(self):
        del self._userDBManger

