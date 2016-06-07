from Project import Attribute

class AttributeSet:
    attributeSetID = 0
    attributeSet = set(Attribute())

    def __init__(self,attributeSetID,attributeSet):
        self.attributeSetID = attributeSetID
        self.attributeSet = attributeSet


    def addAttribute(self,attribute):
        self.attributeSet.add(attribute)

    def removeAttribute(self,attribute):
        self.attributeSet.remove(attribute)


    @property
    def getAttributeSetID(self):
        return self.attributeSetID

    @attributeSetID.setter
    def setAttributeSetID(self,attributeSetID):
        self.attributeSetID = attributeSetID

    @property
    def getAttributeSet(self):
        return self.attributeSet

    @attributeSet.setter
    def setAttributeSet(self,attributeSet):
        self.attributeSet = attributeSet

