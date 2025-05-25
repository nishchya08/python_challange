# Recursion ->

def  fibonacci_iteration(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    a,b = 0,1
    for i in range(2, n+1):
        a, b = b, a+b
    return b
#result= fibonacci_iteration(4)
#print("Fibonacci iteration result: ",result)


def  fibonacci_iteration(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_iteration(n-1) + fibonacci_iteration(n-2)
result= fibonacci_iteration(7)
print("Fibonacci iteration result: ",result)