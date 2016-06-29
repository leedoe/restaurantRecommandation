# -*- encoding=utf-8 -*-

import pymysql
from web.pyscript.Model.Singleton import Singleton
from web.pyscript.Model.FoodPreference import FoodPreference
from web.pyscript.Controller.DBAcountManager import DBAcountManager

class FoodPreferenceDBManager(metaclass=Singleton):

    def __init__(self):
        dbAcountManager = DBAcountManager()
        self._conn = pymysql.connect(host='project.czpuraarclth.ap-northeast-2.rds.amazonaws.com', \
                                     port=3306, user=dbAcountManager.ID, passwd=dbAcountManager.PW, \
                                     db='django', charset='utf8')

    def __del__(self):
        self._conn.close()

    def refresh(self):
        dbAcountManager = DBAcountManager()
        self._conn.close()
        self._conn = pymysql.connect(host='project.czpuraarclth.ap-northeast-2.rds.amazonaws.com',\
                                     port=3306, user=dbAcountManager.ID, passwd=dbAcountManager.PW,\
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

        records.close()
        return result

    def searchUserIDsByFoodIDWithoutUserID(self, foodID, userID):
        '''
        FoodPreference Table에서 찾아서 입력받은 User ID를 제외한 나머지 사용자를 list로 반환
        :param foodID: 음식 ID (integer)
        :param userID: 사용자 ID (integer)
        :return: User ID(integer) list
        '''

        records = self._conn.cursor()
        records.execute("SELECT userID_id FROM web_userfoodpreference WHERE foodID_id=" + str(foodID)\
                        + " AND userID_id!=" + str(userID))
        result = [int(record[0]) for record in records]

        records.close()
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

        records.close()
        return result


    def searchFoodPreferencesByUserID(self, userID):
        '''
        FoodPreference Table에서 찾아서 Preference instance들을 list로 반환
        :param userID: 사용자 ID(integer)
        :return: FoodPreference instance(list)
        '''

        records = self._conn.cursor()
        records.execute("SELECT * FROM web_userfoodpreference WHERE userID_id=" + str(userID))
        result = [FoodPreference(int(record[0]), int(record[1]), int(record[3]), int(record[2])) for record in records]
        records.close()
        return result

    def searchFoodScoresByFoodID(self, foodID):
        '''
        FoodPreference Table에서 찾아서 score들을 list로 반환
        :param foodID: 음식 ID (integer)
        :return: 음식 score (list)
        '''

        records = self._conn.cursor()
        records.execute("SELECT score FROM web_userfoodpreference WHERE foodID_id=" + str(foodID))
        result = [int(score[0]) for score in records]

        records.close()
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

        if records.rowcount <= 0:
            records.close()
            return None

        record = []
        for attrs in records:
            for attr in attrs: record.append(int(attr))

        records.close()
        return FoodPreference(record[0], record[1], record[3], record[2])

    def searchFoodPreferenceScoresByUserID(self, userID):
        '''
        FoodPreference Table에 접근하여 사용자 ID를 이용하여 사용자가 평가한 점수를 반환
        :param userID: 사용자 ID (integer)
        :return: tuple(음식 ID, score) (dictionary)
        '''

        result = dict()

        records = self._conn.cursor()
        records.execute("SELECT score, foodID_id FROM web_userfoodpreference WHERE userID_id=" + str(userID))

        for record in records:
            result[record[1]] = int(record[0])

        return result