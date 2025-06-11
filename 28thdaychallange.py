'''
# python challange
x=3
while x:
    print(x)
    x-=1
'''

# Execution time of python program

import time
# record start time
start=time.time()
print(start)

# Code to measure
result= sum(range(1, 1000001))
print(result)

# Record end time
end=time.time()

execution_time=end - start

print(f"Execution time is {execution_time:.5f} seconds")