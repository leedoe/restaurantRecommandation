from Project import Restaurant
from Project import RestaurantList
from Project import RestaurantDBManager


class RestaurantManager:

    restaurantList = RestaurantList()
    restaurantDBManager = RestaurantDBManager()

    def __init__(self,restaurantList,restaurantDBManager):
        self.restaurantList = restaurantList
        self.restaurantDBManager = restaurantDBManager

    def addRestaurant(self,name,location,foods):
        restaurant = Restaurant(name, location, foods)
        self.restaurantList.restaurantList.append(restaurant)

    def modifyRestaurantByName(self, name, newName):
        for restaurant in self.restaurantList.restaurantList:
            if (restaurant.getName() == name):
                restaurant.setName(newName)
                break

    def modifyRestaurantByLocation(self,name,location):
        for restaurant in self.restaurantList.restaurantList:
            if(restaurant.getName() == name):
                restaurant.setLocation(location)
                break

    def modifyRestaurantByFoods(self, name, foods):
        for restaurant in self.restaurantList.restaurantList:
            if (restaurant.getName() == name):
                restaurant.setFoods(foods)
                break

    def deleteRestaurantByName(self,name):
        for restaurant in self.restaurantList.restaurantList:
            if (restaurant.getName() == name):
                self.restaurantList.restaurantList.remove(restaurant)
                break
