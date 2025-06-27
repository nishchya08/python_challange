#name = input("Enter your name: ")
#while name == "":
#    print("Please enter your name: ")-3
#    name = input("Enter your name: ")

#print(f"Hello {name}")

#age= int(input("Enter your age: "))
#while age < 0:
#    print("age can't be negative")
#    age = int(input("Enter your age: "))
#print(f"Your age is {age}")

#food = input("Enter a food you like(q for quit): ")
#while not food == 'q':
#    print(f"your like {food}")
#    food = input("Enter another food you like(q for quit): ")
#print("I am Over !")

number = int(input("Enter a number between 1-10:"))
while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Enter a number between 1-10:"))
print(f" Your number is {number}")