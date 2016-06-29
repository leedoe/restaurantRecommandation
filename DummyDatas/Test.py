# -*- encoding=utf-8 -*-

from Controller.RecommendationEngine import RecommendationEngine
from Model.User import User

user = User(22, 'aa@aa.com', '1234', 10)
recommendedFood = RecommendationEngine().getFoodRecommendationQueue(user)

print(RecommendationEngine().getWordCloudList(recommendedFood, 20))
