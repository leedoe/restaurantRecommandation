# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Food import Food
from Model.FoodList import FoodList
from Controller.FoodDBManager import FoodDBManager

#음식 객체를 관리하는 매니저 클래스
class FoodManager(metaclass=Singleton):

    # 멤버변수:음식 객체 리스트,음식db매니저
    def __init__(self):
        self._foodList = FoodList()
        self._foodDBManager = FoodDBManager()

    def getFoodAttributesByFoodID(self, foodID):
        '''
        음식 ID(integer)를 이용하여 음식의 속성을 반환
        :param foodID: 음식 ID(integer)
        :return: 해당 음식의 속성(dictionaries)
        '''
        return self._foodDBManager.searchFoodAttributesByFoodID(foodID)


    def getPreferencedFoodAttributesListByUserID(self, userID):
        '''
        사용자 ID(integer)를 이용하여 사용자 선호 음식들의 속성을 반환
        dictionary 들의 list로 반환하지만, 해당 element가 어떤 음식인지는 알 수 없음
        :param userID: 사용자의 ID(integer)
        :return: 해당 사용자의 선호 음식의 속성 dictionaries(list)
        '''
        return self._foodDBManager.searchPreferencedFoodAttributesListByUserID(userID)


    #음식객체를 생성하여 리스트에 추가
    def makeFood(self, foodId, foodName):
        food = Food(foodId, foodName)
        self._foodList.addFoodByFood(food)

    #음식이름으로 리스트에서 음식객체를 반환
    def searchFood(self, foodName):
        return self._foodList.searchFoodByName(foodName)

    # 음식이름으로 리스트에서 음식객체를 삭제
    def deleteFood(self, foodName):
        self._foodList.deleteFood(foodName)

    # 2개의 음식속성값을 비교(음식1 이름,음식2 이름,음식1 속성이름(키),음식2 속성이름(키))
    def compareFoodAttributeValue(self, foodNameA, foodNameB, attributeNameA, attributeNameB):
        foodA = self._foodList.searchFoodByName(foodNameA)
        foodB = self._foodList.searchFoodByName(foodNameB)
        #음식에 속성이름(키)값이 존재하지 않을 경우 거짓
        if attributeNameA not in foodA.attributeDict or attributeNameB not in foodB.attributeDict:
            return False
        attributeSetA = foodA.attributeDict[attributeNameA]
        attributeSetB = foodB.attributeDict[attributeNameB]
        listA = list(attributeSetA)
        listB = list(attributeSetB)
        listA.sort()
        listB.sort()
        if len(listA) != len(listB):#속성개수가 같지 않을 경우 거짓
            return False
        else:
            for i in range(0,len(listA)):
                if(listA[i] != listB[i]):#속성값이 다를 경우 거짓
                    return False
        return True

    # 2개의 음식의 사전에 있는 모든 음식 속성키에 해당하는 속성값을  비교(음식1 이름,음식2 이름,음식1 )
    def compareFoodAttributeKey(self, foodNameA, foodNameB):
        foodA = self._foodList.searchFoodByName(foodNameA)
        foodB = self._foodList.searchFoodByName(foodNameB)
        keyListA = list(foodA.attributeDict.keys())
        keyListB = list(foodB.attributeDict.keys())
        if len(keyListA) != len(keyListB):  # 속성키 개수가 같지 않을 경우 거짓
            return False
        else:
            keyListA.sort()
            keyListB.sort()
            for i in range(0, len(keyListA)):
                if (keyListA[i] != keyListB[i]):  # 속성키가 다를 경우 거짓
                    return False
                else:
                    if self.compareFoodAttributeValue(foodNameA, foodNameB, keyListA[i], keyListB[i]) == False:
                        return False
        return True

    # 음식 속성갑(집합)의 교집합 찾기(음식1 이름,음식2 이름,음식1 속성 키,음식2 속성 키)
    def intersectionFoodAttribute(self, foodNameA, foodNameB, attributeNameA, attributeNameB):
        foodA = self._foodList.searchFoodByName(foodNameA)
        foodB = self._foodList.searchFoodByName(foodNameB)
        attributeSetA = foodA.attributeDict[attributeNameA]
        attributeSetB = foodB.attributeDict[attributeNameB]
        return attributeSetA.intersection(attributeSetB)

    # 음식 속성갑(집합)의 합집합 찾기(음식1 이름,음식2 이름,음식1 속성 키,음식2 속성 키)
    def unionFoodAttribute(self, foodNameA, foodNameB, attributeNameA, attributeNameB):
        foodA = self._foodList.searchFoodByName(foodNameA)
        foodB = self._foodList.searchFoodByName(foodNameB)
        attributeSetA = foodA.attributeDict[attributeNameA]
        attributeSetB = foodB.attributeDict[attributeNameB]
        return attributeSetA.union(attributeSetB)


    @property
    def foodList(self):
        return self._foodList

    @foodList.setter
    def foodList(self, value):
        self._foodList = value

    @foodList.deleter
    def foodList(self):
        del self._foodList

    @property
    def foodDBManager(self):
        return self._foodDBManager

    @foodDBManager.setter
    def foodDBManager(self, value):
        self._foodDBManager = value

    @foodDBManager.deleter
    def foodDBManager(self):
        del self._foodDBManager