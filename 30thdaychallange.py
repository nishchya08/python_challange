
# 1.Python mistake using mutable default arguments

def add_items(item, items=[]):
    items.append(item)
    return items
#Fix

def add_item(item, items=None):
    if items is None:
        items=[]
    items.append(item)
    return items


# 2. Not using list comprehension
result=[]
for i in range(10):
    result.append(i*2)

# fix

result=[i*2 for i in range(10)]