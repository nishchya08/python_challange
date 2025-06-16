# Using print() for Debuging instead of proper Debugging Tools

def calculate(x):
    print(f"Debug: x = {x}")
    return x * 2
result=calculate(5)

def calculate(x):
    return x * 2
result = calculate(5)
# Use a debugger for inspection
import pdb; pdb.set_trace()