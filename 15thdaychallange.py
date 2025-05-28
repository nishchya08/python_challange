# Without running the code tell me the output

for i in range(1,3):
    for j in range(2):
        print(i+j)

# 4 ways to swap 2 numbers in python

# 1.with temp variable
a=5
b=10
temp=a
a=b
b=temp
print("After swapping: a=", a, ", b=", b)

# 2.without temporary variable
a=5
b=10
a=a+b
b=a-b
a=a-b
print("After swapping: a=", a, ", b=", b)

# 3. using tuple unpacking

a=5
b=10
a,b=b,a
print("After swapping: a=", a, ", b=", b)

# Using XOR bitwise operation
a=5
b=10
a=a^b
b=a^b
a=a^b
print("After swapping: a=", a, ", b=", b)