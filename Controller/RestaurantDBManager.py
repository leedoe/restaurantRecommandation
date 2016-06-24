# -*- encoding=utf-8 -*-

import pymysql
from Model.Singleton import Singleton
from Model.Restaurant import Restaurant
from Model.RestaurantFeature import RestaurantFeature
from Controller.DBAcountManager import DBAcountManager

class RestaurantDBManager(metaclass=Singleton):

    def __init__(self):

        dbAcountManager = DBAcountManager()
        self._conn = pymysql.connect(host='project.czpuraarclth.ap-northeast-2.rds.amazonaws.com', \
                                     port=3306, user=dbAcountManager.ID, passwd=dbAcountManager.PW, \
                                     db='recommend', charset='utf8')

    def searchRestaurantsIDsByFoodID(self, foodID):
        '''
        Menu 테이블에 접근하여 음식 ID에 맞는 식당 ID를 얻음
        :param foodID: 음식 ID (integer)
        :return: 식당 ID(integer) 목록 (list)
        '''

        records = self._conn.cursor()
        records.execute('SELECT RestaurantID FROM Menu WHERE FoodID=' + str(foodID))

        result = [int(record[0]) for record in records]

        return result

    def searchRestaurantsByRestaurantID(self, restaurantID):
        '''
        Restaurant 테이블에 접근하여 식당 ID에 맞는 식당 정보를 얻음
        :param restaurantID: 식당 ID (integer)
        :return: Restaurant Class instances (list)
        '''

        records = self._conn.cursor()
        records.execute('SELECT * FROM Restaurant WHERE ID=' + str(restaurantID))

        result = [Restaurant(record[0], record[1], record[2]) for record in records]

        return result

    def searchRestaurantsByRestaurantIDAndLocation(self, restaurantID, location=str()):
        '''
        Restaurant 테이블에 접근하여 식당 ID와 지역에 맞는 식당 정보를 얻음
        :param restaurantID: 식당 ID (integer)
        :param location: 지역 (string)
        :return: Restaurant Class instances (list)
        '''

        records = self._conn.cursor()
        records.execute('SELECT * FROM Restaurant WHERE ID=' + str(restaurantID) + " AND Location='" + location + "'")

        result = [Restaurant(record[0], record[1], record[2]) for record in records]

        return result


    def searchRestaurantFeaturesByRestaurantID(self, restaurantID):
        '''
        RestaurantFeature 테이블에 접근하여 식당 ID에 맞는 식당 정보를 얻음
        :param restaurantID: 식당 ID (integer)
        :return: RestaurantFeature Class instances (list)
        '''

        records = self._conn.cursor()
        records.execute('SELECT * FROM RestaurantFeature WHERE RestaurantID=' + str(restaurantID))

        result = [RestaurantFeature(record[0], record[1], record[2], record[3]) for record in records]

        return result