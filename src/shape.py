import math
###############################################################################################
class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)
        
    def length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))
#################################################################################################
class Shape:
    def __init__(self) -> None:
        self.vertices = []

    def add_vertex(self, p:Point) -> None:
        self.vertices.append(p)

    def __str__(self):
        return f"number of vertices: {len(self.vertices)}"
    
    def perimeter(self) -> float:
        if(len(self.vertices) == 0):
            raise RuntimeError("no vertex aded")
        if (len(self.vertices) > 0):
            P = 0
            for i in range(len(self.vertices)-1):
                X = self.vertices[i+1].x - self.vertices[i].x
                Y = self.vertices[i+1].y - self.vertices[i].y
                P = P + math.sqrt(X*X + Y*Y)
            X = self.vertices[len(self.vertices)-1].x - self.vertices[0].x
            Y = self.vertices[len(self.vertices)-1].y - self.vertices[0].y  
            if (len(self.vertices) == 2):
                return (P + math.sqrt(X*X + Y*Y))/2
            else:
                return P + math.sqrt(X*X + Y*Y)     
        else:
            return 1/0    
#################################################################################################
class Line(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        self.vertices = []   #########################333
        self.add_vertex(p1)  #3########################## NO Member Variable
        self.add_vertex(p2)  ############################
        
        
    def __str__(self):
        p1 = f"Line:\n\tp1: (x : {self.vertices[0].x}, y: {self.vertices[0].y}) \n\t"
        p2 = f"p2: (x : {self.vertices[1].x}, y: {self.vertices[1].y})"
        return (p1 + p2)

    def area(self) -> float:
        return 0

#################################################################################################
class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point) -> None:
        self.vertices = []   #########################333
        self.add_vertex(p1)  #3########################## NO Member Variable
        self.add_vertex(p2)  ############################
        self.add_vertex(p3)  ############################

        
        if((self.vertices[0].x == self.vertices[1].x) and (self.vertices[0].x == self.vertices[2].x)):
            raise RuntimeError("dsdssddssd")

        if((self.vertices[0].y == self.vertices[1].y) and (self.vertices[0].y == self.vertices[2].y)):
            raise RuntimeError("dsdssddssd")

    def __str__(self):
        p1 = f"Triangle:\n\tp1: (x : {self.vertices[0].x}, y: {self.vertices[0].y}) \n\t"
        p2 = f"p2: (x : {self.vertices[1].x}, y: {self.vertices[1].y}) \n\t"
        p3 = f"p3: (x : {self.vertices[2].x}, y: {self.vertices[2].y})"
        return (p1 + p2 + p3) 

    def area(self):
        a1 = self.vertices[0].x * (self.vertices[1].y - self.vertices[2].y)
        a2 = self.vertices[1].x * (self.vertices[2].y - self.vertices[0].y)
        a3 = self.vertices[2].x * (self.vertices[0].y - self.vertices[1].y)
        return abs(a1+a2+a3)/2
#################################################################################################
class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        self.vertices = []   #########################333
        self.add_vertex(p1)  #3########################## NO Member Variable
        self.add_vertex(p2)  ############################
        
    def __str__(self):
        p1 = f"Rect:\n\tp1: (x : {self.vertices[0].x}, y: {self.vertices[0].y}) \n\t"
        p2 = f"p2: (x : {self.vertices[1].x}, y: {self.vertices[0].y}) \n\t"
        p3 = f"p3: (x : {self.vertices[1].x}, y: {self.vertices[1].y}) \n\t"
        p4 = f"p4: (x : {self.vertices[0].x}, y: {self.vertices[1].y})"
        return (p1 + p2 + p3 + p4)
    def area(self):
        return abs((self.vertices[0].x - self.vertices[1].x) * (self.vertices[0].y - self.vertices[1].y)) 
