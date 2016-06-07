import Food.py

from Project import FoodPreference


class User:
    userId = ""
    email = ""
    password = ""
    age = 0
    gender = ""
    foodPreference = []

    def __init__(self, userId, email, password, age, gender, foodPreference):
        self.userId = userId
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.foodPreference = foodPreference

    def addPreference(self, foodName, score):
        food = Food(foodName)
        foodPreference = FoodPreference(score, food)
        self.foodPreference.append(foodPreference)

    def modifyPreference(self, foodName, score):
        for foodPreference in self.foodPreference:
            food = foodPreference.getFood()
            if food.getName() == foodName:
                food.setScore(score)
                break


    def deletePreference(self, foodName):
        for foodPreference in self.foodPreference:
            food = foodPreference.getFood()
            if food.getName() == foodName:
                self.foodPreference.remove(foodPreference)
                break

    @property
    def getFoodPreference(self):
        return self.foodPreference

    @property
    def getUserId(self):
        return self.userId

    @property
    def getEmail(self):
        return self.email

    @property
    def getPassword(self):
        return self.password

    @property
    def getAge(self):
        return self.age

    @property
    def getGender(self):
        return self.gender

    @property
    def getFoodPreference(self):
        return self.foodPreference

    @userId.setter
    def setUserId(self,userId):
        self.userId = userId

    @email.setter
    def setEmail(self,email):
        self.email = email

    @password.setter
    def setPassword(self,password):
        self.password = password

    @age.setter
    def setAge(self,age):
        self.age = age

    @gender.setter
    def setGender(self,gender):
        self.gender = gender

    @foodPreference.setter
    def setFoodPreference(self,foodPreference):
        self.foodPreference = foodPreference