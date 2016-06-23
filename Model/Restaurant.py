#-*- encoding=utf-8 -*-

#식당에 대한 정보를 담고 있는 클래스
class Restaurant:
    # 멤버변수:식당 id,이름,지역 ,음식 리스트
    def __init__(self, ID, name, location):
        self._ID = ID
        self._name = name
        self._location = location

    #식당객체 정보를 출력
    def __repr__(self):
        return "Restaurant{식당ID=%d ,식당명=%s ,식당지역=%s ,음식수=%d}"%(self._restaurantID,self._name,self._location,len(self._foods))

    @property
    def ID(self):
        return self._ID

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location