# 2D list

#fruits = ["apple", "banana", "orange"]
#vegetables =["celery", "carrot", "tomato"]
#meat = ["fish","chicken","turkey"]
groceries = [["apple", "banana", "orange"],
            ["celery", "carrot", "tomato"],
            ["fish","chicken","turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()
