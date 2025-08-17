# @property = Decorator used to define a method as a property. It can be accessed like an attribute, without needing to call it as a method.
# Benefit: Add additional logic when read, write or delete attributes.
# Gives you better, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return f"{self._width} cm"

    @property
    def height(self):
        return f"{self._height} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle1 = Rectangle(10,20)
rectangle1.width = 15  # Using the setter to change width
rectangle1.height = 0  # Using the setter to change height

del rectangle1.width  # Using the deleter to delete width
del rectangle1.height  # Using the deleter to delete height
