import math

class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y


    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def __add__(self,o):
        return self.x + o.x, self.y + o.y
        
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

class Shape:
    def __init__(self) -> None:
        self.vertices = []

class Line(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        pass

class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point) -> None:
        pass

class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        pass