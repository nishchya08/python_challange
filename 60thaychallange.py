# Function() -- A block of reusable code

# def happy_birthday(name, age):
#    print(f"Happy Birthday to {name}")
#    print(f" You are {age} years old")
#    print("Happy Birthday to you")

# happy_birthday("Karuna", 34)
# happy_birthday("Varuna", 28)

# def display_invoice(name, amount, due_date):
#    print(f"Hello {name}")
#    print(f"Your bill of ${amount:.2f} is due on {due_date}")

#display_invoice("Raju", 43.33, "01/04")


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Karuna", "Singh")
print(full_name)