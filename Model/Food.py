#-*- encoding=utf-8 -*-


class Food:

    def __init__(self, ID, name):
        '''
        음식에 관한 정보를 가지고 있는 클래스
        :param ID: 음식 ID (integer)
        :param name: 음식 이름 (string)
        '''
        self.ID = ID
        self.name = name

    def __repr__(self):
        return "Food(ID = %d, name = %s)"%(self.ID, self.name)

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
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name