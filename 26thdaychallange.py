from sympy.physics.units.util import quantity_simplify

# Area of rectangle
"""
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

volume = length * width * height
print(f"The volume is {volume}cm^3")
"""

print("-------------------------------------")

item=input("What item would you like to buy: ")
price=float(input("Enter the price of item: "))
qunantity=int(input("Enter the quantity of items: "))
total = price * qunantity
print(f"You have bought {qunantity} x {item}s")
print(f"Your total is  Rs {total}")
