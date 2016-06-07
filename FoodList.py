from Project import Food


class FoodList:

    foodList = []

    def addFood(self,name,attributeSetMap):
        food = Food(name, attributeSetMap)
        self.foodList.append(food)

    def searchFoodByName(self,name):
        for food in self.foodList:
            if food.getName() == name:
                return food

    def searchFoodByFoodID(self, foodID):
        for food in self.foodList:
            if food.getFoodID() == foodID:
                return food

    def modifyFoodByName(self, name,newName):
        for food in self.foodList:
            if food.getName() == name:
                food.setName(name)
                break

    def modifyFoodByFoodID(self, name, newFoodID):
        for food in self.foodList:
            if food.getName() == name:
                food.setFoodID(newFoodID)
                break

    def modifyFoodByAttributeSetMap(self, name, newAttributeSetMap):
        for food in self.foodList:
            if food.getName() == name:
                food.setAttributeSetMap(newAttributeSetMap)
                break

    def deleteFood(self, name):
        for food in self.foodList:
            if food.getName() == name:
                self.foodList.remove(food)
                break

    @property
    def getFoodList(self):
        return self.foodList

    @foodList.setter
    def setFoodList(self,foodList):
        self.foodList = foodList