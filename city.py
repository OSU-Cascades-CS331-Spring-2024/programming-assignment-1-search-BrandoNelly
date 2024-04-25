class City():

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = {}

    def add_neighbor(self, city, distance):
        self.neighbors[city] = distance

    def get_neighbors(self):
        return self.neighbors.keys()
