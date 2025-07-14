# Abstract class : A class that can not be instantiated on its own; Meant to be subclassed
#                  They can contain abstract methods, which are declared but no implementation.
#                  Abstract classes benefits:
#                  1. Prevent instantiation on the class itself
#                  2. Requires children to use inherited subclasses

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def go(self):
        print(" You drive the car")

    def stop(self):
        print(" You stop the car")

#car = car()
#car.go()
#car.stop()

class Motorcycle(vehicle):
    def go(self):
        print(" You ride the motorcycle")

    def stop(self):
        print(" You stop the motorcycle")
#motorcycle = Motorcycle()
#motorcycle.go()
#motorcycle.stop()

class Boat(vehicle):
    def go(self):
        print(" You sail the boat")
    def stop(self):
        print(" You anchor the boat")

boat = Boat()
boat.go()
boat.stop()



