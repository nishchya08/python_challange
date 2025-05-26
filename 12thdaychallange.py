# Exception handling in Functions
from turtledemo.sorting_animate import enable_keys


def lst():
    lst_input= input("Enter the items (space separated): ").split()
    index = int(input("Enter the index of the item: "))
    try:
        element = lst_input[index]
        print(element)
    except IndexError:
        print("invalid Index Input")
    print("Thank you")
lst()
