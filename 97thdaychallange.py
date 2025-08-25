# exception = An event that interupt the flow of an program
#             (ZeroDivisionError, IndexError, KeyError)
#               1. try:
#               2. except:
#               3. finally:

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("you can't divide by zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here.")
