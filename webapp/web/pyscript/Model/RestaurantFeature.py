# -*- encoding=UTF-8 -*-

class RestaurantFeature:

    def __init__(self, ID, restaurantID, name, contents):
        '''
        식당에 관한 정보를 가지고 있는 클래스
        :param ID: 식당 특징 ID (integer)
        :param restaurantID: 식당 ID (integer)
        :param name: 특징 이름 (integer)
        :param contents: 특징 목록 (string)
        '''
        self.ID = ID
        self.restaurantID = restaurantID
        self.name = name
        self.contents = contents

    def __repr__(self):
        contents = ''
        for content in self.contents:
            contents += content + ', '
        contents = contents[:-2]
        return "FoodAttribute(ID = %d, RestaurantID = %d, FeatureName = %s, contents = %s)" \
               % (self.ID, self.restaurantID, self.name, contents)


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
    def restaurantID(self):
        return self._restaurantID

    @restaurantID.setter
    def restaurantID(self, restaurantID):
        self._restaurantID = restaurantID

    @restaurantID.deleter
    def restaurantID(self):
        del self._restaurantID

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
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, contents):
        self._contents = set([content.strip() for content in contents.split(',')])

    @contents.deleter
    def contents(self):
        del self._contents