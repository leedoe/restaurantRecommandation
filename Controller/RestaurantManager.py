# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Model.Restaurant import Restaurant
from Controller.RestaurantDBManager import RestaurantDBManager

#식당 객체를 관리하는 매니저 클래스
class RestaurantManager(metaclass=Singleton):

    # 멤버변수:식당 객체 리스트 객체,식당db매니저 객체
    def __init__(self):
        self._restaurantDBManager = RestaurantDBManager()
