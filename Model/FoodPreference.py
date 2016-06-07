#-*- encoding=utf-8 -*-

class FoodPreference:

    def __init__(self):
        self._foodPreferenceID = int
        self._food = str()
        self._score = int

    def getScore(self):
        return self._score