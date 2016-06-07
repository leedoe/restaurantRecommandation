class RestaurantList:

    restaurantList = []

    def __init__(self,restaurantList):
        self.restaurantList = restaurantList

    def getRestaurantList(self):
        return self.restaurantList

    def setRestaurantList(self,restaurantList):
        self.restaurantList = restaurantList

    def searchRestaurantByName(self, name):
        for restaurant in self.restaurantList:
            if restaurant.getName() == name:
                return restaurant

    def searchRestaurantByLocation(self, location):
        for restaurant in self.restaurantList:
            if restaurant.getLocation() == location:
                return restaurant

    def searchRestaurantByFoods(self, foods):
        for restaurant in self.restaurantList:
            if restaurant.getFoods() == foods:
                return restaurant

    def searchRestaurantByFood(self, food):
        restaurantList = []
        for restaurant in self.restaurantList:
            for food in restaurant.getFoods:
                if food.getName() == food:
                    restaurantList.append(restaurant)
                    break
                return restaurantList

    def modifyRestaurantByName(self,name,newName):
        for restaurant in self.restaurantList:
            if restaurant.getName() == name:
                restaurant.setName(newName)
                break

    def modifyRestaurantByLocation(self, name, newLocation):
        for restaurant in self.restaurantList:
            if restaurant.getName() == name:
                restaurant.setLocation(newLocation)
                break

    def modifyRestaurantByFoods(self, name, newFoods):
        for restaurant in self.restaurantList:
            if restaurant.getName() == name:
                restaurant.setFoods(newFoods)
                break

    def deleteRestaurantByName(self, name):
        for restaurant in self.restaurantList:
            if restaurant.getName() == name:
                self.restaurantList.remove(restaurant)
                break

    @property
    def getRestaurantList(self):
        return self.restaurantList

    @restaurantList.setter
    def setRestaurantList(self,restaurantList):
        self.restaurantList = restaurantList