class Restaurant:
    restaurantID = 0
    name = ""
    location = ""
    foods = []

    def __init__(self, name, location, foods):
        self.restaurantID = 0
        self.name = name
        self.location = location
        self.foods = foods

    def __init__(self, restaurantID, name, location, foods):
        self.restaurantID = restaurantID
        self.name = name
        self.location = location
        self.foods = foods

    @property
    def getRestaurantID(self):
        return self.restaurantID

    @property
    def getName(self):
        return self.name

    @property
    def getLocation(self):
        return self.location

    @property
    def getFoods(self):
        return self.foods

    @restaurantID.setter
    def setRestaurantID(self,restaurantID):
        self.restaurantID = restaurantID

    @name.setter
    def setName(self,name):
        self.name = name

    @location.setter
    def setLocation(self,location):
        self.location = location

    @foods.setter
    def setFoods(self,foods):
        self.foods = foods
