class AttributeSetMap:
    map = {}

    def __init__(self, map):
        self.map = map

    def addAttributeSet(self, attributeSetCode, attributeSet):
        map[attributeSetCode] = attributeSet

    def addElementInAttributeSet(self, attributeSetCode, element):
        map[attributeSetCode].add(element)

    def searchAttributeSet(self, attributeSetCode):
        return map[attributeSetCode]

    def searchElementInAttributeSet(self, attributeSetCode, element):
        list = list(map[attributeSetCode])
        for i in list:
            if element == i:
                return True
        return False

    def modifyAttributeSetCode(self, oldAttributeSetCode, newAttributeSetCode):
        map[newAttributeSetCode] = map[oldAttributeSetCode]
        del map[oldAttributeSetCode]

    def modifyElementInAttributeSet(self, attributeSetCode, newElement):
        map[attributeSetCode] = newElement

    def deleteAttributeSet(self, attributeSetCode):
        del map[attributeSetCode]

    def deleteElementInAttributeSet(self, attributeSetCode, element):
        list = list(map[attributeSetCode])
        for i in list:
            if element == i:
                del list[i]
                break

    @property
    def getMap(self):
        return self.map

    @map.setter
    def setMap(self,map):
        self.map = map
