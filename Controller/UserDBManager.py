# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton

class UserDBManger(metaclass=Singleton):

    # db에 user정보 삽입
    def insertUser(self,user):
        pass

    # db에 user정보 삭제
    def deleteUser(self,user):
        pass

    # db에 user정보 수정
    def modifyUser(self,user):
        pass

    # db에 user정보 검색
    def searchUser(self,user):
        pass

