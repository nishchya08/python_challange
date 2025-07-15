# "Duck Typing" --> Another way to achieve polymorphism behind inheritance
#                   Objects must have minimum necessary attributes/methods
#                   "If it looks like a duck and quacks like a duck, it must be a duck.
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class car:
    alive = True
    def speak(self):
        print("HORN")

animals = [Dog(), Cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)