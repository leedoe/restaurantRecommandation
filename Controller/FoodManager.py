# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Food import Food
from Model.FoodList import FoodList
from Controller.FoodDBManager import FoodDBManager

#음식 객체를 관리하는 매니저 클래스
class FoodManager:
    __metaclass__ = Singleton

    def __init__(self):
        self._foodList = []
        self._foodDBManager = FoodDBManager()

    def makeFood(self, name, attributeSetMap):
        food = Food(name, attributeSetMap)
        self.foodList.foodList.append(food)

    def searchFood(self, foodName):
        for food in self.foodList.foodList:
            if food.getName() == foodName:
                return food

    def deleteFood(self, foodName):
        for food in self.foodList.foodList:
            if food.getName() == foodName:
                self.foodList.foodList.remove(food)

    def compareFoodAttribute(self, foodNameA, foodNameB, attributeSetCodeA, attributeSetCodeB):
        attributeSetMapA = foodNameA.getAttributeSetMap()
        attributeSetMapB = foodNameB.getAttributeSetMap()
        if (attributeSetMapA[attributeSetCodeA] == attributeSetMapB[attributeSetCodeB]):
            return True
        return False

    def intersectionFoodAttribute(self, foodNameA, foodNameB, attributeSetCodeA, attributeSetCodeB):  # 교집합 찾기
        for food in self.foodList.foodList:
            if food.name == foodNameA:
                attributeSetMapA = food.attributeSetMap
            if food.name == foodNameB:
                attributeSetMapB = food.attributeSetMap
        return attributeSetMapA[attributeSetCodeA].intersection(attributeSetMapB[attributeSetCodeB])

    def intersectionFoodAttribute(self, foodA, foodB, attributeSetCodeA, attributeSetCodeB):
        attributeSetMapA = foodA.attributeSetMap
        attributeSetMapB = foodB.attributeSetMap
        return attributeSetMapA[attributeSetCodeA].intersection(attributeSetMapB[attributeSetCodeB])

    def unionFoodAttribute(self, foodNameA, foodNameB, attributeSetCodeA, attributeSetCodeB):  # 합집합 찾기
        for food in self.foodList.foodList:
            if food.name == foodNameA:
                attributeSetMapA = food.attributeSetMap
            if food.name == foodNameB:
                attributeSetMapB = food.attributeSetMap
        return attributeSetMapA[attributeSetCodeA].union(attributeSetMapB[attributeSetCodeB])

    def unionFoodAttribute(self, foodA, foodB, attributeSetCodeA, attributeSetCodeB):
        attributeSetMapA = foodA.attributeSetMap
        attributeSetMapB = foodB.attributeSetMap
        return attributeSetMapA[attributeSetCodeA].union(attributeSetMapB[attributeSetCodeB])

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