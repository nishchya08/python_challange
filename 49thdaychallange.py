# Shopping car program

foods = []
prices = []
total =0

while True:
    food = input("What food do you want to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price =float(input("What the price of {food}: $ "))
        foods.append(food)
        prices.append(price)
print("--- YOUR CART ---")
for food in foods:
    print(food, end= " ")
for price in prices:
    total+=price
print()
print(f"Your total is: ${total}")


