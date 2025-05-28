# python challange without run please tell me the output
from pstats import func_std_string

n=0
while n<4:
    n+=1
    if n==3:
        continue
    print(n)

print("-----------------------------------------")

func=[]
for i in range(5):
    func.append(lambda x=i: x)
print([f() for f in func])

print("------------------------------")

for i in range(1,10,3):
    print(i)
    if(i==4):
        break
print("-----------------------")

data=[(1,3),(3,1),(2,3)]
sorted_data=sorted(data, key=lambda x:x[0])
print(sorted_data)


print("---------------")


from collections import deque
dq= deque([1,2,3])
dq.append(4)
print(dq)

