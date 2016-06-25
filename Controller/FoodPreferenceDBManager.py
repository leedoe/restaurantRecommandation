# -*- encoding=utf-8 -*-

import pymysql
from Model.Singleton import Singleton
from Model.FoodPreference import FoodPreference
from Controller.DBAcountManager import DBAcountManager

class FoodPreferenceDBManager(metaclass=Singleton):

    def __init__(self):
        dbAcountManager = DBAcountManager()
        self._conn = pymysql.connect(host='project.czpuraarclth.ap-northeast-2.rds.amazonaws.com', \
                                     port=3306, user=dbAcountManager.ID, passwd=dbAcountManager.PW, \
                                     db='django', charset='utf8')


    def searchUserIDsByFoodID(self, foodID):
        '''
        FoodPreference Table에서 찾아서 user ID(integer)들을 list로 반환
        :param foodID: FoodPreference Table에서 찾을 음식 ID
        :return: User ID(integer) (list)
        '''

        records = self._conn.cursor()
        records.execute("SELECT userID_id FROM web_userfoodpreference WHERE foodID_id=" + str(foodID))

        result = [int(record[0]) for record in records]

        return result


    def searchFoodIDsByUserID(self, userID):
        '''
        FoodPreference Table에서 찾아서 food ID(integer)들을 list로 반환
        :param userID: FoodPreference Table에서 찾을 음식 ID
        :return: food ID(integer) (list)
        '''

        records = self._conn.cursor()
        records.execute("SELECT foodID_id FROM web_userfoodpreference WHERE userID_id=" + str(userID))

        result = [int(record[0]) for record in records]

        return result


    def searchFoodPreferencesByUserID(self, userID):
        '''
        FoodPreference Table에서 찾아서 Preference instance들을 list로 반환
        :param userID: 사용자 ID(integer)
        :return: FoodPreference instance(list)
        '''

        records = self._conn.cursor()
        records.execute("SELECT id, score, foodID_id, userID_id FROM web_userfoodpreference WHERE userID_id=" + str(userID))

        result = [FoodPreference(int(record[0]), int(record[1]), int(record[2]), int(record[3])) for record in records]

        return result

    def searchFoodPreferenceByUserIDAndFoodID(self, userID, foodID):
        '''
        Food Preference Table에서 사용자 ID와 음식 ID가 맞는 레코드를 찾아서 FoodPreference instance로 반환
        :param userID: 사용자 ID (integer)
        :param foodID: 음식 ID (integer)
        :return: FoodPreference Class (instance), 존재하지 않는 경우 None
        '''

        records = self._conn.cursor()
        records.execute("SELECT id, score, foodID_id, userID_id FROM web_userfoodpreference "\
                        + "WHERE foodID_id=" + str(foodID) + " AND userID_id=" + str(userID))

        if records.rowcount <= 0: return None

        record = []
        for attrs in records:
            for attr in attrs: record.append(int(attr))

        return FoodPreference(record[0], record[1], record[2], record[3])