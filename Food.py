from Project import AttributeSetMap


class Food:
    foodID = 0
    name = ""
    attributeSetMap = AttributeSetMap()

    def __init__(self, name):
        self.name = name
        self.foodID = 0
        self.attributeSetMap = AttributeSetMap()

    def __init__(self, name, attributeSetMap):
        self.name = name
        self.attributeSetMap = attributeSetMap

    def __init__(self, foodID, name, attributeSetMap):
        self.foodID = foodID
        self.name = name
        self.attributeSetMap = attributeSetMap

    @property
    def getName(self):
        return self.name

    @property
    def getFoodID(self):
        return self.foodID

    @property
    def getAttributeSetMap(self):
        return self.attributeSetMap

    @name.setter
    def setName(self,name):
        self.name = name

    @foodID.setter
    def setFoodID(self, foodID):
        self.foodID = foodID

    @attributeSetMap.setter
    def setAttributeSetMap(self, attributeSetMap):
        self.attributeSetMap = attributeSetMap

