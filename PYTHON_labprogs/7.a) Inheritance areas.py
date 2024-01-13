class Shape:
    def __init__(self):
        self.name=""
        self.area=0.0
    def show(self):
        print(self.name,"has the area",self.area)

class Circle(Shape):
    def __init__(self,r):
        super().__init__()
        self.name="Circle"
        self.area=3.14*r*r

class Triangle(Shape):
    def __init__(self,b,h):
        super().__init__()
        self.name="Triangle"
        self.area=0.5*b*h

class Rectangle(Shape):
    def __init__(self,l,b):
        super().__init__()
        self.name="Rectangle"
        self.area=l*b

c=Circle(float(input("Enter the radius : ")))
c.show()

t=Triangle(float(input("Enter the base and height : ")),float(input()))
t.show()

r=Rectangle(float(input("Enter the length and breadth : \t")),float(input()))
r.show()