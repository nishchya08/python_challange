# Exception handling

try:
    a=10
    b=0
    print(a/b)
except TypeError:
    print("Non-Integer value has been occured")
except ZeroDivisionError:
    print("Division by zero has been occured")
else:
    print("This is getting printed using the else block")
finally:
    print("This will get executed everytime")