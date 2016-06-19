#-*- encoding=utf-8 -*-

#음식속성에 대한 정보를 담고 있는 클래스
class Attribute:
    # 멤버변수:속성 이름
    def __init__(self,name):
        self._name = name

    # 음식속성 객체 정보를 출력
    def __repr__(self):
        return "Attribute{음식속성명=%s}" % (self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

