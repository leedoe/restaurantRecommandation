#-*- encoding=utf-8 -*-

from Model.Attribute import Attribute

#음식속성에 대한 정보를 집합으로 관리하는 클래스
class AttributeSet:
    # 멤버변수:집합id,음식 속성 집합
    def __init__(self,attributeSetID):
        self._attributeSetID = attributeSetID
        self._attributeSet = set()

    #속성 집합에 속성을 추가
    def addAttribute(self,attribute):
        self._attributeSet.add(attribute)

    #속성 집합에 속성을 제거
    def removeAttribute(self,attribute):
        self._attributeSet.remove(attribute)


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
