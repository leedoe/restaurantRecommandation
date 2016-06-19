#-*- encoding=utf-8 -*-

#식당에 대한 정보를 담고 있는 클래스
class Restaurant:
    # 멤버변수:식당 id,이름,지역 ,음식 리스트
    def __init__(self, restaurantID, name, location):
        self.restaurantID = restaurantID
        self.name = name
        self.location = location
        self.foods = []

    @property
    def restaurantID(self):
        return self._restaurantID

    @restaurantID.setter
    def restaurantID(self, value):
        self._restaurantID = value

    @restaurantID.deleter
    def restaurantID(self):
        del self._restaurantID


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


    @property
    def location(self):
        return self._location

    @location.setter
    def location(self,value):
        self._location = value

    @location.deleter
    def location(self):
        del self._location


    @property
    def foods(self):
        return self._foods

    @foods.setter
    def foods(self,value):
        self._foods = value

    @foods.deleter
    def foods(self):
        del self._foods