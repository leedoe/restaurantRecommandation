#-*- encoding=utf-8 -*-

class User:

    def __init__(self, email, password, age, gender):
        self._email = email
        self._password = password
        self._age = age
        self._gender = gender
        self._foodPreferences = []

    def addPreference(self):
        pass

    def modifyPreference(self):
        pass

    def deletePreference(self):
        pass