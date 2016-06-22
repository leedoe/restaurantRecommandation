# -*- encoding=utf-8 -*-

from Model.Singleton import Singleton
from Controller.FoodPreferenceDBManager import FoodPreferenceDBManager

class FoodDBManager(metaclass=Singleton):

    def __init__(self):
        self._foodPreferenceDBManager = FoodPreferenceDBManager()

    def searchFoodAttributesByFoodID(self, foodID):
        '''
        FoodAttribute Table에 접근하여 Food ID(integer)를 이용해 해당 음식의 속성을 반환
        :param foodID: Food ID(integer)
        :return: 음식 속성(dictionary)
        '''

        result = dict()

        with open('./../DummyDatas/foodAttributes.txt', 'r', encoding='UTF8') as attributes:
            for attribute in attributes:
                infos = [info.strip() for info in attribute.split(',')] # [0 = ID, 1 = foodID, 2 = attributeName, 3 = contents]

                if foodID == int(infos[1]):
                    contents = [content.strip() for content in infos[3].split(':')]
                    result[infos[2]] = set(contents)

        return result


    def searchPreferencedFoodAttributesListByUserID(self, userID):
        '''
        해당 사용자의 모든 선호 음식에 대한 속성을 반환
        :param userID: 사용자 ID(integer)
        :return: 음식 속성 dictionaries(list)
        '''

        result = []
        foodIDs = self._foodPreferenceDBManager.searchFoodIDsByUserID(userID)

        for foodID in foodIDs:
            result.append(self.searchFoodAttributesByFoodID(foodID))

        return result