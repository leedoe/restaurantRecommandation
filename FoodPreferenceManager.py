from Project import FoodPreferenceDBManager

class FoodPreferenceManager:
    foodPreferenceDBManger = FoodPreferenceDBManager()

    def __init__(self,foodPreferenceDBManger):
        self.foodPreferenceDBManger=foodPreferenceDBManger


    def getUsersByFoodName(self,foodName):
        self.foodPreferenceDBManger.searchUsersByFoodName(foodName)

    def getFoodsByUserID(self,id):
        self.foodPreferenceDBManger.searchFoodsByUserID(id)

    @property
    def getFoodPreferenceDBManger(self):
        return self.foodPreferenceDBManger

    @foodPreferenceDBManger.setter
    def setFoodPreferenceDBManager(self,foodPreferenceDBManger):
        self.foodPreferenceDBManger =foodPreferenceDBManger