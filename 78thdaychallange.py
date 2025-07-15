# super() = Fucntion used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inhrited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
#        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a cricle with an area of  {3.14 * self.radius * self.radius}cm^2")
        

class Square(Shape):
    def __init__(self,color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width
circle = Circle(color='red', is_filled=True, radius=2)

#print(circle.color)
#print(circle.is_filled)
#print(f"{circle.radius}cm")
circle.describe()