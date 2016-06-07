from Project import Food
from Project import FoodList
from Project import FoodDBManager


class FoodManager:
    foodList = FoodList()
    foodDBManger = FoodDBManager()

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
    def getFoodList(self):
        return self.foodList

    @foodList.setter
    def setFoodList(self, foodList):
        self.foodList = foodList
