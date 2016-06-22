# -*- encoding=utf-8 -*-

from Controller.RecommendationEngine import RecommendationEngine
from Model.User import User

user = User(1, 'aa@aa.com', '1234', 10)
recommendedFood = RecommendationEngine().runMapping(user)

print(recommendedFood)
print(recommendedFood.pop())
print(recommendedFood.pop())
print(recommendedFood.pop())