# Coding challange

def combine(f, g):
    return lambda x: f(g(x))
f = lambda x: x ** 2
g= lambda x: x + 2
h=combine(f,g)
print(h(4))

# output 25