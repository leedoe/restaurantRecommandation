# -*- encoding=UTF-8 -*-

class RestaurantFeature:

    def __init__(self, ID, restaurantID, name, contents):
        self._ID = ID
        self._restaurantID = restaurantID
        self._name = name
        self._contents = contents


    @property
    def ID(self):
        return self._ID

    @property
    def restaurantID(self):
        return self._restaurantID

    @property
    def name(self):
        return self._name

    @property
    def contents(self):
        return self._contents
