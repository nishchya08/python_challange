#  Excessive Function Calls

# Inefficient

def process_item(item):
    print(item)

my_list=[1,2,3,4,5]
for i in range(len(my_list)):
    process_item(my_list[i])

# Efficient
# Use local variables or inline code where funcion calls are unnecessary
def process_item(item):
    print(item)

items=[1,2,3,4,5]
for item in items:
    process_item(item)
