#-*- encoding=utf-8 -*-

from Model.Food import Food

#음식정보 객체를 리스트로 관리하는 클래스
class FoodList:

    # 멤버변수:음식 객체 리스트
    def __init__(self):
        self._foodList = []

    #음식 객체 타입으로 음식 추가 _ 성공여부 반환
    def addFoodByFood(self,food):
        #음식이름 중복 검사 중복시 false 반환
        for foodTmp in self._foodList:
            if foodTmp.name == food.name:
                return False
        #음식이름 비중복시 리스트에 삽입후 true 반환
        self._foodList.append(food)
        return True

    # 음식id와 이름으로 음식 추가 _ 성공여부 반환
    def addFoodByIdAndName(self, foodID, name):
        # 음식id 와 이름으로 중복 검사 중복시 false 반환
        for foodTmp in self._foodList:
            if foodTmp.name == name | foodTmp.foodId == foodID:
                return False
                # 음식id 또는 이름 비중복시 리스트에 삽입후 true 반환
        food = Food(foodID, name)
        self._foodList.append(food)
        return True

    #이름으로 음식객체 검색 _ 검색된 객체 반환
    def searchFoodByName(self,name):
        for food in self._foodList:
            if food.name == name:
                return food

    #이름id로 음식객체 검색 _ 검색된 객체 반환
    def searchFoodByFoodID(self, foodID):
        for food in self._foodList:
            if food.foodID == foodID:
                return food

    #음식이름 변경 _ 성공여부 반환
    def modifyFoodByName(self, name,newName):
        for food in self._foodList:
            if food.name== name:
                food.name = newName
                return True
        return False

    # 음식id 변경 _ 성공여부 반환
    def modifyFoodByFoodID(self, name, newFoodID):
        #변경할 음식id가 기존 음식 리스트에 있는지 검사 _ 있다면 바꿀 수 없다
        for food in self._foodList:
            if food.foodID == newFoodID:
                return False
        for food in self._foodList:
            if food.name == name:
                food.foodID = newFoodID
                return True
        return False

    # 음식속성 집합 맵 변경 _ 성공여부 반환
    def modifyFoodByAttributeSetMap(self, name, newAttributeSetMap):
        for food in self._foodList:
            if food.name == name:
                food.attributeSetMap = newAttributeSetMap
                return True
        return False

    # 음식 이름으로 리스트에서 음식 객체 삭제
    def deleteFood(self, name):
        for food in self._foodList:
            if food.name == name:
                self._foodList.remove(food)
                return True
        return False

    @property
    def foodList(self):
        return self._foodList

    @foodList.setter
    def foodList(self,value):
        self._foodList = value

    @foodList.deleter
    def foodList(self):
        del self._foodList