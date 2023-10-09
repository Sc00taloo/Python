import math
import secrets

class Shape():
    color = ""
    def __init__(self, points):
       self.points = points
    def square(self, point):
        pass
    def perimeter(self, point):
        pass
    def move(self, dx, dy):
        for point in self.points:
            point[0] += dx
            point[1] += dy
    def fill(color):
        print(color)
    def compare(self, x, y):
        if x > y:
            print("Первая фигура больше второй")
        elif x == y:
            print("Они равны")
        else:
            print("Вторая фигура больше первой")
    def is_intersect(self, x, y):
        pass
        #flag = True
        #x_coords1 = [x.points[0] for point in self.points]
        #y_coords1 = [x.points[1] for point in self.points]
        #x_coords2 = [y.points[0] for point in self.points]
        #y_coords2 = [y.points[1] for point in self.points]
    def is_include(self, x, y):
        pass
        #flag = True
        #x_coords1 = [x.points[0] for point in self.points]
        #y_coords1 = [x.points[1] for point in self.points]
        #x_coords2 = [y.points[0] for point in self.points]
        #y_coords2 = [y.points[1] for point in self.points]
        #for i in range (len(x.points)):
        #    if x.points[i] < y.points[i]:
        #        flag = False
        #        return flag
        #for i in range (len(y_coords1)):
        #    if y_coords1[i] < y_coords2[i]:
        #        flag = False
        #        return flag
        #return flag

class quadrilateral(Shape):
    def __init__(self, points):
        super().__init__(points)
    def perimeter(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5)
        BC = ((x_coords[2] - x_coords[1]) ** (2) + (y_coords[2] - y_coords[1]) ** (2)) ** (0.5)
        CD = ((x_coords[3] - x_coords[2]) ** (2) + (y_coords[3] - y_coords[2]) ** (2)) ** (0.5)
        DA = ((x_coords[0] - x_coords[3]) ** (2) + (y_coords[0] - y_coords[3]) ** (2)) ** (0.5)
        return AB + BC + CD + DA
    def square(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5)
        BC = ((x_coords[2] - x_coords[1]) ** (2) + (y_coords[2] - y_coords[1]) ** (2)) ** (0.5)
        CD = ((x_coords[3] - x_coords[2]) ** (2) + (y_coords[3] - y_coords[2]) ** (2)) ** (0.5)
        DA = ((x_coords[0] - x_coords[3]) ** (2) + (y_coords[0] - y_coords[3]) ** (2)) ** (0.5)
        perim = AB + BC + CD + DA
        return (perim * (perim - AB) * (perim - BC) * (perim - CD) * (perim - DA)) ** (0.5)

class quadra(Shape):
    def __init__(self, points):
        super().__init__(points)
    def perimeter(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5)
        return AB * 2
    def square(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5)
        return AB * AB

class correctPentagon(Shape):
    def __init__(self, points):
        super().__init__(points)
    def other_points(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5)  
        x2 = (x_coords[0] + x_coords[1])/2 + AB * math.sin(math.radians(72))/math.sin(math.radians(36))
        y2 = (y_coords[0] + y_coords[1])/2 + AB * math.cos(math.radians(72))/math.sin(math.radians(36))
        x3 = (x2 + x2)/2 - (x_coords[1] - x2) * math.sin(math.radians(72))/math.sin(math.radians(36))
        y3 = (y2 + y2)/2 - (y_coords[1] - y2) * math.sin(math.radians(72))/math.sin(math.radians(36))
        x4 = (x3 + x2)/2 - AB * math.sin(math.radians(72))/math.sin(math.radians(36))
        y4 = (y3 + y2)/2 - AB * math.cos(math.radians(72))/math.sin(math.radians(36))
        return [(x_coords[0], y_coords[0]), (x_coords[1], y_coords[1]), (x2, y2), (x3, y3), (x4, y4)]
    def perimeter(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5)     
        return AB * 5
    def square(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        AB = ((x_coords[1] - x_coords[0]) ** (2) + (y_coords[1] - y_coords[0]) ** (2)) ** (0.5) 
        return  AB ** (2) / 4 * (25 + 10 * (5) ** (0.5)) ** (0.5)

points1 = [(0, 0), (0, 4), (4, 4), (4, 0)]
result1 = quadra(points1)

points2_1 = [(0, 0), (0, 4)]
pentagon = correctPentagon(points2_1)
other_points = pentagon.other_points()
result2 = correctPentagon(other_points)

points3 = [(1, 4),(3,6),(0, 3),(1,2)]
result3 = quadrilateral(points3)

points4 = [(6, 1),(10,5),(3, 6),(1,3)]
result4 = quadrilateral(points4)

points5 = [(1, 3), (1, 6), (4, 6), (4, 3)]
result5 = quadra(points5)

points6 = [(3, 0), (3, 8), (11, 8), (11, 0)]
result6 = quadra(points6)

points7_1 = [(3, 6), (4, 2)]
pentagon = correctPentagon(points7_1)
other_points = pentagon.other_points()
result7 = correctPentagon(other_points)

points8_1 = [(10, 0), (10, 4)]
pentagon = correctPentagon(points8_1)
other_points = pentagon.other_points()
result8 = correctPentagon(other_points)

points9 = [(3, 4),(7, 4),(4, 5),(2, 5)]
result9 = quadrilateral(points9)

points10 = [(10, 2),(6, 6),(8, 6),(10,5)]
result10 = quadrilateral(points10)

points11 = [(5, 4),(3, 6),(3, 10),(7, 6)]
result11 = quadrilateral(points11)

points12_1 = [(1, 1), (6, 1)]
pentagon = correctPentagon(points12_1)
other_points = pentagon.other_points()
result12 = correctPentagon(other_points)

points13 = [(1, 1), (1, 3), (3, 3), (3, 1)]
result13 = quadra(points13)

points14 = [(4, 1), (4, 6), (9, 6), (9, 1)]
result14 = quadra(points14)

points15 = [(10, 5), (10, 6), (11, 6), (11, 5)]
result15 = quadra(points15)

shapes = [result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11, result12, result13, result14, result15 ]
color = ["red", "green", "yellow", "blue", "pink", "brown"]

for shape in shapes:
    print(f"Perimeter: {shape.perimeter()}")
    print(f"Square: {shape.square()}")
    shape.color = secrets.choice(color)
    print(f"Color: {shape.color}")
    print("---")

for i in range (len(shapes)):
    for j in range (i + 1, len(shapes)):
        print(f"Comparison results for: {i + 1}",)
        print(shapes[i].compare(shapes[i].square(), shapes[j].square()))
       # print(f"Intersection results for: {i + 1}",)
       # print(shapes[i].is_intersect(shapes[i], shapes[j]))
        print(f"Inclusion results for: {i + 1}",)
        print(shapes[i].is_include(shapes[i], shapes[j]))
        print("-")
    print("---")