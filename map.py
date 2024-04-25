class Map():

    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.cities = {}

    def add_city(self, city):
        self.cities[city.name] = city

    def get_city(self, name):
        return self.cities.get(name)
    
    def get_all_cities(self):
        return self.cities.values()
