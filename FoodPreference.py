from Project import Food


class FoodPreference:
    foodPreferenceID = 0
    score = 0
    food = Food()

    def __init__(self, foodPreferenceID, score, food):
        self.foodPreferenceID = foodPreferenceID
        self.score = score
        self.food = food

    def __init__(self,  score, food):
        self.foodPreferenceID = 0
        self.score = score
        self.food = food

    @foodPreferenceID.setter
    def setFoodPreferenceID(self, foodPreferenceID):
        self.foodPreferenceID = foodPreferenceID

    @score.setter
    def setScore(self, score):
        self.score = score

    @food.setter
    def setFood(self,food):
        self.food = food

    @property
    def getFood(self):
        return self.food

    @property
    def getScore(self):
        return self.food

    @property
    def getFoodPreferenceID(self):
        return self.foodPreferenceID