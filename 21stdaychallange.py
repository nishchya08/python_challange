# Overusing the Global Variables

# Infficient

result=0
def add(x):
    global result
    result+=x
add(5)

# Efficient

def add(x, total):
    return total+x

result=0
result=add(5, result)
print(result)