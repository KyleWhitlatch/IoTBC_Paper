import math

class invalid_distance(Exception):
    "distance is too far"

class grid():
    def __init__(self):
        self.x_size = 100
        self.y_size = 100
        self.MAX_DIST = 100
        self.edges = {}
        self.iots = {}
        self.grid = [["" for _ in range(100)] for _ in range(100)]

    def add_iot(self, id, coords):
        try:
            for edge in self.edges:
                if math.dist(list(coords), list(self.edges[edge])) > self.MAX_DIST:
                    raise invalid_distance
                else:
                    self.iots[id] = coords
                    self.grid[coords[1]][coords[0]] = 'i'
                    print('iot added')
        except invalid_distance:
            print("iot too far from edge, deleted")

    def add_edge(self, id, coords):
        self.edges[id] = tuple(coords)
        self.grid[coords[1]][coords[0]] = 'e'

    def closest_edge(self, iot):
        i = self.iots[iot]
        min_dist = self.MAX_DIST
        edge = 0
        for e in self.edges:
            if math.dist(list(i), list(self.edges[e])) < min_dist:
                min_dist = math.dist(list(i), list(self.edges[e]))
                edge = e
        return edge

    def print_grid(self):
        for x in range(100):
            print(str(grid[99-x]))

