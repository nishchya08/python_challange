
# Small challanges

for i in range(10,0,-2):
    if i<5:
        break
    print(i)
print("----------------------------------------")


from functools import reduce
numbers=[1,2,3,4]
f= lambda  x: x * 2
g= lambda lst: reduce(lambda a,b : a + b, lst)
print(f(g(numbers)))
print("--------------------------------------------")


def combine(f,g):
    return lambda x: f(g(x))
f =lambda x: x*2
g=lambda x: x+3
h= combine(f,g)
print(h(4))
print("------------------------------")


def append_item(val, lst=[]):
# lst=[] is a mutable default argument
'''
In python, default argument values are evaluated once when the fucntion is defined, not each time it's called
That means the same lit(lst) is reused across multiple calls unless a new one is explicitly provided
'''

    lst.append(val)
    return lst
print(append_item(1))
print(append_item(2))

