# When to use append method

items=['bag', 'book', 'pencil', 'pen']
result= []
for item in items:
    if len(item)== 3:
        result.append(item.upper())
print(result)

# when to use extend method

"""
Use the extend() method when you want to concentrate two lists or add multiple elements too= an iterable ,
 It's a more efficient way to combine lists. For example, if you want to extend a list by elements from a nested list, you can use the extend()
  method with a for loop
  """
nested_list = [[4,5,6],[7,8,9]]
my_list= [1,2,3]
for item in nested_list:
    my_list.extend(item)
print(my_list)