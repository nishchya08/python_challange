# Keyword arguments = an argument prceeded by an indentifier
#                      helps with readibility
#                      order of argument does not matter
#                       1. Positional 2. default 3. KEYWORD 4. arbitrary
from itertools import count


#def greeting(greet, title, first_name, last_name ):
#    print(greet, title, first_name, last_name)

# print(greeting("Hello", title="Miss", last_name="Singh", first_name="Karuna"))


def get_phone(country,area, first, last):
    return  f"{country}-{area}-{first}-{last}"

phone = get_phone(country=1, area=123, first=456, last=789)
print(phone)