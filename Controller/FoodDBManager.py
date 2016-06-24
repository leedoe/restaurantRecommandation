# -*- encoding=utf-8 -*-

import pymysql
from Model.Singleton import Singleton
from Model.FoodAttribute import FoodAttribute
from Controller.DBAcountManager import DBAcountManager
from Controller.FoodPreferenceDBManager import FoodPreferenceDBManager

class FoodDBManager(metaclass=Singleton):

    def __init__(self):
        self._foodPreferenceDBManager = FoodPreferenceDBManager()

        dbAcountManager = DBAcountManager()
        self._conn = pymysql.connect(host='project.czpuraarclth.ap-northeast-2.rds.amazonaws.com',\
                                     port=3306, user=dbAcountManager.ID, passwd=dbAcountManager.PW,\
                                     db='recommend', charset='utf8')

    def searchFoodAttributesByFoodID(self, foodID):
        '''
        FoodAttribute Table에 접근하여 Food ID(integer)를 이용해 해당 음식의 속성을 반환
        :param foodID: Food ID(integer)
        :return: 음식 속성 (dictionary)
        '''

        result = dict()

        records = self._conn.cursor()
        records.execute('SELECT AttributeName, contents FROM FoodAttribute WHERE FoodID=' + str(foodID))

        for record in records:
            contents = [content.strip() for content in record[1].split(',')]
            result[record[0]] = set(contents)

        return result


    def searchPreferencedFoodAttributesListByUserID(self, userID):
        '''
        해당 사용자의 모든 선호 음식에 대한 속성을 반환
        :param userID: 사용자 ID (integer)
        :return: 음식 속성 dictionaries (list)
        '''

        result = []
        foodIDs = self._foodPreferenceDBManager.searchFoodIDsByUserID(userID)

        for foodID in foodIDs:
            result.append(self.searchFoodAttributesByFoodID(foodID))

        return result