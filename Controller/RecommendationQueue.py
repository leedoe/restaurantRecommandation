#-*- encoding=utf-8 -*-

class RecommendationQueue:
    def __init__(self, foodSet, foodDict):
        # 각 음식을 하나씩 꺼내서 Queue에 넣는 작업을 한다.
        # 해당 Queue의 top은 [1]이다.
        self._queue = [['UNDERFLOW']]
        for food in foodSet:
            mean = count = 0 # 평균과 count는 0으로
            for groupInfo in foodDict[food]:
