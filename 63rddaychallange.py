# *args = allow you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple keyword-arguments


#def display_name(*args):
#    for arg in args:
#        print(arg, end= " ")
# display_name("Nishchya", "Kataria")

def house_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
house_details(street= "123 Fake st.",
              city = "San Francisco",
              state = "CA",
              zipcode = "12345")
