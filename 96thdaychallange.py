# recursion = a function that calls itself from within
#              helps to visualize a complex problem into basic steps,
#              which can be solved more easily iteratively or recursively

# ITERATIVE
# def walk(steps):
#     for step in range(1, steps + 1):
#         print(f"you take step #{step}")

# walk(5)

# ITERATIVE
# def factorial(n):
#     result=1
#     for i in range(n):
#         result *= (i+1)
#     return result

# RECURSIVE

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))