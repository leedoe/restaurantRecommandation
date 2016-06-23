#-*- encoding=utf-8 -*-


#음식에 대한 정보를 담고 있는 클래스
class Food:
    # 멤버변수:음식 id,음식 이름,속성 집합 맵
    def __init__(self, foodID, name):
        self._foodID = foodID
        self._name = name

    #속성이름을 키로 속성집합을 값으로 딕셔너리에 저장(음식이름(키),음식속성 집합(값))
    def addAttribute(self,attributeName,attributeSet):
        self._attributeSetDict[attributeName] = attributeSet

    # 음식객체 정보를 출력
    def __repr__(self):
        return "Food{음식ID=%d ,음식명=%s }"%(self._foodID,self._name)

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name