# Inheritance = Allow a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class child(parent)

class Animal():
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("meeuuuuiii")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Smarty")
cat = Cat("muchu")
mouse = Mouse("montu")

#print(dog.name)
#print(cat.is_alive)
#dog.eat()
#cat.sleep()
#mouse.eat()
dog.speak()
mouse.speak()