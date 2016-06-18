#-*- encoding=utf-8 -*-

from Model.AttributeSetMap import AttributeSetMap

class Food:

    def __init__(self, foodID, name):
        self._foodID = foodID
        self._name = name
        self._attributeSetMap = AttributeSetMap()
        self._flavors = []

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

