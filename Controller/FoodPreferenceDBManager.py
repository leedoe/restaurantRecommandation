# -*- encoding=utf-8 -*-

import pymysql
from Model.Singleton import Singleton
from Model.FoodPreference import FoodPreference

class FoodPreferenceDBManager(metaclass=Singleton):

    def searchUserIDsByFoodID(self, foodID):
        '''
        FoodPreference Table에서 찾아서 user ID(integer)들을 list로 반환
        :param foodID: FoodPreference Table에서 찾을 음식 ID
        :return: User ID(integer) (list)
        '''
        result = []

        with open('./../DummyDatas/foodPreferences.txt', 'r', encoding='UTF8') as preferences:
            for infos in preferences:
                info = [int(parse) for parse in infos.split(',')] # (0 = ID, 1 = score, 2 = userID, 3 = foodID)
                if info[3] == foodID:
                    result.append(info[2])


        return result


    def searchFoodIDsByUserID(self, userID):
        '''
        FoodPreference Table에서 찾아서 food ID(integer)들을 list로 반환
        :param userID: FoodPreference Table에서 찾을 음식 ID
        :return: food ID(integer) (list)
        '''
        result = []

        with open('./../DummyDatas/foodPreferences.txt', 'r', encoding='UTF8') as preferences:
            for infos in preferences:
                info = [int(parse) for parse in infos.split(',')]  # (0 = ID, 1 = score, 2 = userID, 3 = foodID)
                if info[2] == userID:
                    result.append(info[3])


        return result


    def searchFoodPreferencesByUserID(self, userID):
        '''
        FoodPreference Table에서 찾아서 Preference instance들을 list로 반환
        :param userID: 사용자 ID(integer)
        :return: FoodPreference instance(list)
        '''
        result = []

        with open('./../DummyDatas/foodPreferences.txt', 'r', encoding='UTF8') as preferences:
            for infos in preferences:
                info = [int(parse) for parse in infos.split(',')] # (0 = ID, 1 = score, 2 = userID, 3 = foodID)
                if info[2] == userID:
                    result.append(FoodPreference(info[0], info[1], info[2], info[3]))


        return result

    def searchFoodPreferenceByUserIDAndFoodID(self, userID, foodID):
        '''
        Food Preference Table에서 사용자 ID와 음식 ID가 맞는 레코드를 찾아서 FoodPreference instance로 반환
        :param userID: 사용자 ID (integer)
        :param foodID: 음식 ID (integer)
        :return: FoodPreference Class (instance), 존재하지 않는 경우 None
        '''

        with open('./../DummyDatas/foodPreferences.txt', 'r', encoding='UTF8') as preferences:
            for infos in preferences:
                info = [int(parse) for parse in infos.split(',')]  # (0 = ID, 1 = score, 2 = userID, 3 = foodID)
                if info[2] == userID and info[3] == foodID:
                    return FoodPreference(info[0], info[1], info[2], info[3])

        return None