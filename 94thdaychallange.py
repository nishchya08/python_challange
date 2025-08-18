# map() = Applies a given function to all items in a collection

#def c_to_f(temp):
#    return (temp * 9/5) + 32
celsius_temps = [0.0, 10.0, 30.0, 40.0, 50.0]
#fahrenheit_temps = list(map(c_to_f, celsius_temps))
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

print(fahrenheit_temps)
#print(celsius_temps)
#print(fahrenheit_temps)

#for temp in fahrenheit_temps:
#    print(temp)