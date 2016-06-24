# -*- encoding=UTF-8 -*-

from Model.Singleton import Singleton

class DBAcountManager(metaclass=Singleton):

    def __init__(self):
        with open('./../DBInfo', 'r', encoding='UTF8') as file:
            self.ID = file.readline()
            self.PW = file.readline()

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID.strip('\n')

    @property
    def PW(self):
        return self._PW

    @PW.setter
    def PW(self, PW):
        self._PW = PW.strip('\n')