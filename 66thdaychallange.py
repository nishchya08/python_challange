# List comprehension

# doubles = [ x * 2 for x in range(1,11) ]
# print(doubles)

# fruits = ["apple", "banana", "cherry"]
# fruits = [fruit.upper() for fruit in fruits]
# fruits =[fruit[0] for fruit in fruits]
# print(fruits)

# numbers = [1,-3,2,-5,6]
# numbers = [ num for num in numbers if num >= 0]
# print(numbers)

grades = [85,65,45,89,32,43,67]
passing_grades = [grade for grade in grades if grade >=60]
print(passing_grades)