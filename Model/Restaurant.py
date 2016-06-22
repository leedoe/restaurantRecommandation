#-*- encoding=utf-8 -*-

#식당에 대한 정보를 담고 있는 클래스
class Restaurant:
    # 멤버변수:식당 id,이름,지역 ,음식 리스트
    def __init__(self, restaurantID, name, location):
        self._restaurantID = restaurantID
        self._name = name
        self._location = location
        self._foods = []

    # 음식을 추가하다
    def addFood(self, food):
        #기존에 음식이 있는지 확인 있으면 거짓 반환
        for foodTmp in self._foods:
            if foodTmp.name == food.name:
                return False
        #없으면 음식 추가
        self._foods.append(food)
        return True

    #식당객체 정보를 출력
    def __repr__(self):
        return "Restaurant{식당ID=%d ,식당명=%s ,식당지역=%s ,음식수=%d}"%(self._restaurantID,self._name,self._location,len(self._foods))

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