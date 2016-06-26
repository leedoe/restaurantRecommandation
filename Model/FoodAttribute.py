#-*- encoding=utf-8 -*-


class FoodAttribute:

    def __init__(self, ID, foodID, name, contents):
        '''
        음식 속성에 관한 정보를 가지고 있는 클래스
        :param ID: 음식 속성 ID (integer)
        :param foodID: 음식 ID (integer)
        :param name: 속성 이름 (string)
        :param contents: 속성 목록 (string)
        '''
        self.ID = ID
        self.foodID = foodID
        self.name = name
        self.contents = contents

    def __repr__(self):
        contents = ''
        for content in self.contents:
            contents += content + ', '
        contents = contents[:-2]
        return "FoodAttribute(ID = %d, foodID = %d, attributeName = %s, contents = %s)" % (self.ID, self.foodID, self.name, contents)

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
    def foodID(self):
        return self._foodID

    @foodID.setter
    def foodID(self, foodID):
        self._foodID = foodID

    @foodID.deleter
    def foodID(self):
        del self._foodID

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self, name):
        del self._name

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, contents):
        self._contents = set([content.strip() for content in contents.split(',')])

    @contents.deleter
    def contents(self):
        del self._contents

