#-*- encoding=utf-8 -*-


class FoodAttribute:

    def __init__(self, ID, foodID, name, contents):
        self._ID = ID
        self._foodID = foodID
        self._name = name
        # contents에 대해서 입력을 set으로 저장하는 것이 필요함.

    # 음식속성 객체 정보를 출력
    def __repr__(self):
        return "Attribute Class instance : ID = %d, foodID = %d, name = %s, contents " % (self._ID, self._foodID, self._name)

    @property
    def ID(self):
        return self._ID

    @property
    def foodID(self):
        return self._foodID

    @property
    def name(self):
        return self._name

    @property
    def contents(self):
        return self._contents

