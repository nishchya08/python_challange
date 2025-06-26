# Python scope rule(LEGB Rule)
'''
x=10
def example():
    print(x)
    x=5
example()

'''

# Fix
x=10
def example():
    global x
    print(x)
    x=5
example()