# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton

class UserManager:
    __metaclass__ = Singleton

    def __init__(self):
        self._userDBManager
        pass

    def searchUserByEmail(self):
        pass

    def makeUser(self):
        pass

    def modifyUser(self):
        pass

    def deleteUser(self):
        pass

    def getUserPreferences(self):
        pass