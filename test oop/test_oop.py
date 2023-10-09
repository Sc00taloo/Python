class Point:  
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def dist(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

pos1 = Point(3, 1)
pos2 = Point(2, 1)
print(pos1.dist(pos2))
print("sTOP")
