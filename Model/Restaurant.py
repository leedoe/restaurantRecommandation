#-*- encoding=utf-8 -*-


class Restaurant:

    def __init__(self, ID, name, location):
        '''
        식당에 관한 정보를 가지고 있는 클래스
        :param ID: 식당 ID (integer)
        :param name: 식당 이름 (string)
        :param location: 식당 지역 (string)
        '''
        self.ID = ID
        self.name = name
        self.location = location


    def __repr__(self):
        return "Restaurant(ID = %d, name = %s, location = %s)"%(self.ID, self.name, self.location)

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @location.deleter
    def location(self):
        del self._location