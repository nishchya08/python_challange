unit = input("Is the temperature in Celcius or Fahrenheit (C/F): ")
temperature = float(input("Enter the temperature: "))
if unit == "F":
    temp = round((temperature * 9 / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}  {unit}")
elif unit == "C":
    temp = round((temperature - 32) * 5/9, 1)
    print(f"The temperature in Celcius is: {temp}  {unit}")
else:
    print(f"{unit} is invalid unit of mesurement")