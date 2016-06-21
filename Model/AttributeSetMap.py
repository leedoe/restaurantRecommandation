#-*- encoding=utf-8 -*-

#음식속성집합을 딕셔너리로 관리하는 클래스
class AttributeSetMap:
    # 멤버변수:음식속성집합 딕셔너리
    def __init__(self):
        self._attSetMap = {}

    def addAttributeSet(self, attributeSetCode, attributeSet):
        self._attSetMap[attributeSetCode] = attributeSet

    def addElementInAttributeSet(self, attributeSetCode, element):
        self._attSetMap[attributeSetCode].add(element)

    def searchAttributeSet(self, attributeSetCode):
        return self._attSetMap[attributeSetCode]

    def searchElementInAttributeSet(self, attributeSetCode, element):
        list = enumerate(self._attSetMap[attributeSetCode])
        for i in list:
            if element == i:
                return True
        return False

    def modifyAttributeSetCode(self, oldAttributeSetCode, newAttributeSetCode):
        self._attSetMap[newAttributeSetCode] = self._attSetMap[oldAttributeSetCode]
        del self._attSetMap[oldAttributeSetCode]

    def modifyElementInAttributeSet(self, attributeSetCode, newElement):
        self._attSetMap[attributeSetCode] = newElement

    def deleteAttributeSet(self, attributeSetCode):
        del self._attSetMap[attributeSetCode]

    def deleteElementInAttributeSet(self, attributeSetCode, element):
        list = enumerate(self._attSetMap[attributeSetCode])
        for i in list:
            if element == i:
                del list[i]
                break

    @property
    def attSetMap(self):
        return self.self._attSetMap

    @attSetMap.setter
    def attSetMap(self,value):
        self.self._attSetMap = value

    @attSetMap.deleter
    def attSetMap(self):
        del self.self._attSetMap

