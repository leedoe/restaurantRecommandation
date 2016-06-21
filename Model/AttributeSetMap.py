#-*- encoding=utf-8 -*-

#음식속성집합을 딕셔너리로 관리하는 클래스
class AttributeSetMap:
    # 멤버변수:음식속성집합 딕셔너리
    def __init__(self):
        self._map = {}

    def addAttributeSet(self, attributeSetCode, attributeSet):
        map[attributeSetCode] = attributeSet

    def addElementInAttributeSet(self, attributeSetCode, element):
        map[attributeSetCode].add(element)

    def searchAttributeSet(self, attributeSetCode):
        return map[attributeSetCode]

    def searchElementInAttributeSet(self, attributeSetCode, element):
        list = enumerate(map[attributeSetCode])
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
    def map(self):
        return self._map

    @map.setter
    def map(self,value):
        self._map = value

    @map.deleter
    def map(self):
        del self._map

