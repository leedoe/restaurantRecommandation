#-*- encoding=utf-8 -*-

from Model.Restaurant import Restaurant

#식당정보 객체를 리스트로 관리하는 클래스
class RestaurantList:

    # 멤버변수:식당 객체 리스트
    def __init__(self):
        self._restaurantList = []

    # 식당 객체 타입으로 식당 추가 _ 성공여부 반환
    def addRestaurant(self,restaurant):
        # 식당이름 중복 검사 중복시 false 반환
        for restaurantTmp in self._restaurantList:
            if restaurantTmp.name == restaurant.name:
                return False
        # 식당이름 비중복시 리스트에 삽입후 true 반환
        self._restaurantList.append(restaurant)
        return True

    #식당명으로 식당객체 검색 _ 검색된 객체 반환
    def searchRestaurantByName(self, name):
        for restaurant in self._restaurantList:
            if restaurant.name == name:
                return restaurant

    #식당주소로 식당객체 검색 _ 검색된 객체 리스트 반환
    def searchRestaurantByLocation(self, location):
        restaurantList = []
        for restaurant in self._restaurantList:
            if restaurant.location == location:
                restaurantList.append(restaurant)
        return restaurantList


    # 음식명으로 식당객체  검색 _ 검색된 식당객체 리스트 반환
    def searchRestaurantByFoodnName(self,foodName):
        restaurantList = []
        for restaurant in self._restaurantList:
            foods =  restaurant.foods
            for foodTmp in foods:
                if foodTmp.name == foodName:
                    restaurantList.append(restaurant)
                    break
        return restaurantList

    #식당이름 변경 _ 성공여부 반환
    def modifyRestaurantByName(self,name,newName):
        for restaurant in self._restaurantList:
            if restaurant.name == name:
                restaurant.name = newName
                return True
        return False

    #식당주소 변경 _ 성공여부 반환
    def modifyRestaurantByLocation(self, name, newLocation):
        for restaurant in self._restaurantList:
            if restaurant.name == name:
                restaurant.location = newLocation
                return True
        return False

    #식당음식 리스트 변경 _ 성공여부 반환
    def modifyRestaurantByFoods(self, name, newFoods):
        for restaurant in self._restaurantList:
            if restaurant.name == name:
                restaurant.foods = newFoods
                return True
        return False

    #식당 이름으로 리스트에서 식당 객체 삭제 _ 성공여부 반환
    def deleteRestaurantByName(self, name):
        for restaurant in self._restaurantList:
            if restaurant.name == name:
                self._restaurantList.remove(restaurant)
                break


    @property
    def restaurantList(self):
        return self._restaurantList

    @restaurantList.setter
    def restaurantList(self,value):
        self._restaurantList = value

    @restaurantList.deleter
    def restaurantList(self):
        del self._restaurantList

