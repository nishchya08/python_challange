# object = A "bundle" of related attributes(variables) and methods(functions)
#                  Ex. phone, cup, book
# You need a class to create many objects

# class = (blueprint) used to design the structure and layout of an project

class car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f" You drive the {self.model}")

    def stop(self):
        print(f" You stop the {self.model}")

car1 = car('Posche',2024,'grey', False)
#print(car1.model)
car1.drive()