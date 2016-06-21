#-*- encoding=utf-8 -*-

from Model.Attribute import Attribute

class AttributeSet:

    def __init__(self,attributeSetID):
        self._attributeSetID = attributeSetID
        self._attributeSet = ()


    def addAttribute(self,attribute):
        self.attributeSet.add(attribute)

    def removeAttribute(self,attribute):
        self.attributeSet.remove(attribute)


    @property
    def attributeSetID(self):
        return self._attributeSetID

    @attributeSetID.setter
    def setAttributeSetID(self,value):
        self._attributeSetID = value

    @attributeSetID.deleter
    def setAttributeSetID(self):
        del self._attributeSetID

    @property
    def attributeSet(self):
        return self._attributeSet

    @attributeSet.setter
    def attributeSet(self,value):
        self._attributeSet = value

    @attributeSet.deleter
    def attributeSet(self):
        del self._attributeSet
