#-*- encoding=utf-8 -*-

from Model.AttributeSetMap import AttributeSetMap

#음식에 대한 정보를 담고 있는 클래스
class Food:
    # 멤버변수:음식 id,음식 이름,속성 집합 맵,음식의 맛 리스트
    def __init__(self, foodID, name):
        self._foodID = foodID
        self._name = name
        self._attributeSetMap = AttributeSetMap()
        self._flavors = []

    #음식의 맛을 추가하다
    def addFlavor(self,flavor):
        self._flavors.append(flavor)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


    @property
    def foodID(self):
        return self._foodID

    @foodID.setter
    def foodID(self, value):
        self._foodID = value

    @foodID.deleter
    def foodID(self):
        del self._foodID


    @property
    def attributeSetMap(self):
        return self._attributeSetMap

    @attributeSetMap.setter
    def attributeSetMap(self, value):
        self._attributeSetMap = value

    @attributeSetMap.deleter
    def attributeSetMap(self):
        del self._attributeSetMap


    @property
    def flavors(self):
        return self._flavors

    @flavors.setter
    def flavors(self,value):
        self._flavors = value

    @flavors.deleter
    def flavors(self):
        del self._flavors

