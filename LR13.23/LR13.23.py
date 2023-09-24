import math

class Shape():
    def __init__(self):
        print('Figure')
    def square(self, a, b):
        return self.a * self.b
    def perimeter(self, a, b):
        return self.a + self.b * 2
    def move(self):
        pass
    def fill(self, color):
        self.color = color
    def compare(self, x, y):
        print(self.x == self.y)
    def is_intersect(self, x, y):
        pass
    def is_include(self,x,y):
        pass

from tkinter import *
 
x = 400
y = 400
n = 5
r = 50

coords=[(x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(1, n+1)]
root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()
reactQuadra = canvas.create_rectangle(100, 100, 150, 150, fill="Blue")
rect4 = canvas.create_polygon(200, 260, 200, 300, 300, 300, 300, 250, fill="Brown")
reactTrue = canvas.create_polygon((coords), fill="Yellow")
root.mainloop()